import json
import re
import datetime

from dataclasses import dataclass, field, InitVar, asdict
from invoke import task, run, Result, Context
import humanize
import tabulate

import edwh
import edwh.tasks


@dataclass
class Bucket:
    js: InitVar[dict] = None
    ctx: InitVar[Context] = None
    quick: InitVar[bool] = None
    name: str = field(init=False)
    size: int = field(init=False)
    hsize: str = field(init=False)
    visibility: str = field(init=False, repr=False)
    file_count: int = field(init=False)

    def __post_init__(self, js: dict, ctx: Context, quick: bool = False):
        self.name = js["bucketName"]
        bucket_info = json.loads(
            ctx.run(
                f'b2 get-bucket {"" if quick else "--showSize"} {self.name}',
                hide=True,
            ).stdout
        )
        self.visibility = bucket_info["bucketType"]
        self.size = bucket_info.get("totalSize", -1)
        self.file_count = bucket_info.get("fileCount", -1)
        self.hsize = humanize.naturalsize(self.size)


@task
def authenticate(c):
    try:
        # ensure bucketname is present, but don't use it right now.
        edwh.tasks.get_env_value("B2_ATTACHMENTS_BUCKETNAME")
        b2_keyid = edwh.tasks.get_env_value("B2_ATTACHMENTS_KEYID")
        b2_key = edwh.tasks.get_env_value("B2_ATTACHMENTS_KEY")
    except FileNotFoundError:
        print("Please run this command in an `omgeving` with a docker-compose.yml!")
        exit(1)

    c.run(f"b2 authorize-account {b2_keyid} {b2_key}")


@task(
    iterable=["bucket"],
    aliases=("bucket", "buckets"),
    help=dict(
        quick="Do not request sizes",
        bucket="(repeatable) bucket name or regexp to filter bucketnames against. ",
        purge="default: False; Purge files updated more than <purge> days ago. ",
        purge_filter="default: .*\\.(tgz|log|gz); Select only these files to purge (to prevent accidental removal) ",
    ),
)
def list_buckets(ctx, quick=False, bucket=None, purge=None, purge_filter=r".*\.(tgz|log|gz)"):
    print("loading bucket overview")
    all_buckets = {b["bucketName"]: b for b in json.loads(ctx.run("b2 list-buckets --json", hide=True).stdout)}

    print("filtering buckets")
    buckets_js = []
    if not bucket:
        buckets_js.extend(all_buckets.values())
    else:
        buckets_js.extend(
            value
            for bucket_name, value in all_buckets.items()
            if any(re.match(bucket_arg, bucket_name) for bucket_arg in bucket)
        )

    print("fetching details")
    buckets = []
    for idx, bucket in enumerate(buckets_js):
        print(f"loading bucket {idx}/{len(buckets_js)}")
        buckets.append(bucket := Bucket(bucket, ctx, quick))

    print(tabulate.tabulate([asdict(b) for b in buckets], headers="keys"))

    if not purge:
        exit()

    max_delta = datetime.timedelta(int(purge) if purge.isdigit() else 100)
    for idx, bucket in enumerate(buckets):
        _purge_bucket(ctx, bucket, buckets, idx, max_delta, purge_filter)


def _purge_bucket(
    ctx: Context,
    bucket: Bucket,
    buckets: list[Bucket],
    idx: int,
    max_delta: datetime.timedelta,
    purge_filter: str,
):
    print(f"Processing {idx}/{len(buckets)} buckets, name: {bucket.name}")
    file_list = json.loads(ctx.run(f"b2 ls --json {bucket.name} --recursive", hide=True).stdout)

    print(f"> Processing {len(file_list)} files.")
    now = datetime.datetime.now()
    to_remove_files = [
        file
        for file in file_list
        if (now - datetime.datetime.fromtimestamp(file["uploadTimestamp"] / 1000)) > max_delta
        and re.match(purge_filter, file["fileName"])
    ]

    print(
        f'> Removing {humanize.naturalsize(sum(f["size"] for f in to_remove_files))} '
        f"in {len(to_remove_files)} of {len(file_list)} files."
    )
    if not edwh.tasks.confirm(f"Removing {len(to_remove_files)} files, are you sure?"):
        # stop
        return

    for idx, file in enumerate(to_remove_files):
        print(f'removing {idx}/{len(to_remove_files)}: {file["fileName"]}')
        ctx.run(
            f'b2 delete-file-version "{file["fileName"]}" "{file["fileId"]}"',
            hide=True,
        )
