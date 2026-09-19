import json
import re

from aws_rag_eval.paths import CORPUS_DIR

# Loads the metadata.json filed and turns it into a dict comprehension.
def load_metadata() -> dict:
    records = json.loads((CORPUS_DIR / "metadata.json").read_text())
    return {record["file"]: record for record in records}

# Removes new line character and parses heading of the text and cleans any whitespace around the text
def split_on_headings(text: str) -> list[str]:
    pieces = re.split(r"\n(?=#)", text)
    return [piece.strip() for piece in pieces if piece.strip()]

# Splits text into chunks also add overlap.
def char_split(section: str, chunk_size: int, overlap: int) -> list[str]:
    if len(section) < chunk_size:
        return [section]

    pieces = []
    start = 0

    while start < len(section):
        pieces.append(section[start : start + chunk_size])
        start += chunk_size - overlap
    return pieces

#Main functions that creates chunks from metadata.
def build_chunks(chunk_size=500, overlap=50) -> list[dict]:
    meta = load_metadata()
    chunks = []
    # Grab md files from corpus
    for path in CORPUS_DIR.glob("*.md"):
        filename = path.name
        # skip file if not in continue
        if filename not in meta:
            continue
        record = meta[filename]

        text = path.read_text(encoding="utf-8")
        sections = split_on_headings(text)

        for section in sections:
            pieces = char_split(section, chunk_size, overlap)
            for piece in pieces:
                chunk = {
                    "id": f"{filename}::{len(chunks)}",
                    "text": piece,
                    "metadata": {
                        "service": record["service"],
                        "title": record["title"],
                        "url": record["url"],
                        "source_file": filename,
                    },
                }
                chunks.append(chunk)
    return chunks


if __name__ == "__main__":
    built = build_chunks()
    print(len(built))
    # for chunk in built[:3]:
    #     print(chunk["id"], " | ", chunk["metadata"]["source_file"], " | ", chunk["text"][:80])
    # for term in ["Access-Control-Allow-Headers", "TTL", "stage variable",
    #          "$context", "eventual consistency", "ARN format", "reserved concurrency"]:
    #     hits = {c["metadata"]["source_file"] for c in build_chunks() if term in c["text"]}
    #     print(term, "->", hits or "NOT FOUND")