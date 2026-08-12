"""
Corpus grabber for the AWS-docs RAG project.

Downloads markdown twins of AWS developer guide pages into corpus/.

Run:  uv run python scripts/grab_corpus.py
"""

import json
import time
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = PROJECT_ROOT / "corpus"

SERVICES = [
    (
        "dynamodb",
        "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/",
        [
            "Introduction",
            "HowItWorks.CoreComponents",
            "HowItWorks.ReadWriteCapacityMode",
            "HowItWorks.Partitions",
            "HowItWorks.NamingRulesDataTypes",
            "SQLtoNoSQL",
            "SecondaryIndexes",
            "GSI",
            "LSI",
            "WorkingWithItems",
            "WorkingWithTables.Basics",
            "Query",
            "Scan",
            "bp-partition-key-design",
            "bp-indexes",
            "bp-query-scan",
            "ProvisionedThroughput",
            "HowItWorks.ProvisionedThroughput",
            "BestPractices",
            "DynamoDBMapper.OptimisticLocking",
            "Expressions.ConditionExpressions",
            "Expressions.UpdateExpressions",
            "ServiceQuotas",
            "Streams",
            "GlobalTables",
            "backuprestore_HowItWorks",
            "PointInTimeRecovery",
            "DAX",
        ],
    ),
    (
        "lambda",
        "https://docs.aws.amazon.com/lambda/latest/dg/",
        [
            "welcome",
            "lambda-foundation",
            "gettingstarted-concepts",
            "lambda-invocation",
            "invocation-sync",
            "invocation-async",
            "invocation-eventsourcemapping",
            "configuration-function-common",
            "configuration-envvars",
            "configuration-concurrency",
            "lambda-runtimes",
            "runtimes-context",
            "lambda-permissions",
            "access-control-resource-based",
            "configuration-layers",
            "configuration-versions",
            "configuration-aliases",
            "monitoring-cloudwatchlogs",
            "lambda-dlq",
            "invocation-retries",
        ],
    ),
    (
        "s3",
        "https://docs.aws.amazon.com/AmazonS3/latest/userguide/",
        [
            "Welcome",
            "UsingBucket",
            "creating-buckets-s3",
            "storage-class-intro",
            "object-lifecycle-mgmt",
            "versioning-workflows",
            "bucketnamingrules",
            "access-control-overview",
            "s3-encryption",
            "IAmazonS3",
        ],
    ),
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def grab() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    metadata = []
    failures = []

    for service, base_url, slugs in SERVICES:
        for slug in slugs:
            url = f"{base_url}{slug}.md"
            try:
                resp = requests.get(url, headers=HEADERS, timeout=20)
            except requests.RequestException as e:
                failures.append((service, slug, f"request error: {e}"))
                continue

            if resp.status_code != 200:
                failures.append((service, slug, f"HTTP {resp.status_code}"))
                continue

            text = resp.text
            title = extract_title(text, slug)
            filename = f"{service}_{slug}.md"
            (OUT_DIR / filename).write_text(text, encoding="utf-8")

            metadata.append(
                {
                    "service": service,
                    "slug": slug,
                    "url": url,
                    "title": title,
                    "file": filename,
                }
            )
            print(f"  ok   {filename}  ({len(text):,} chars)")
            time.sleep(0.5)

    (OUT_DIR / "metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )

    print(f"\nSaved {len(metadata)} pages to {OUT_DIR}/")
    print(f"Metadata written to {OUT_DIR}/metadata.json")

    if failures:
        print(f"\n{len(failures)} failed (top these up from the guide index):")
        for service, slug, reason in failures:
            print(f"  MISS {service}_{slug}  -> {reason}")


if __name__ == "__main__":
    grab()
