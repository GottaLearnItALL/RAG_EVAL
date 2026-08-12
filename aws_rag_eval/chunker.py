import json
import re

from aws_rag_eval.paths import CORPUS_DIR


def load_metadata() -> dict:
    records = json.loads((CORPUS_DIR / "metadata.json").read_text())
    return {record["file"]: record for record in records}


def split_on_headings(text: str) -> list[str]:
    pieces = re.split(r"\n(?=#)", text)
    return [piece.strip() for piece in pieces if piece.strip()]


def char_split(section: str, chunk_size: int, overlap: int) -> list[str]:
    if len(section) < chunk_size:
        return [section]

    pieces = []
    start = 0

    while start < len(section):
        pieces.append(section[start : start + chunk_size])
        start += chunk_size - overlap
    return pieces


def build_chunks(chunk_size=500, overlap=50) -> list[dict]:
    meta = load_metadata()
    chunks = []

    for path in CORPUS_DIR.glob("*.md"):
        filename = path.name

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
    for chunk in built[:3]:
        print(chunk["id"], " | ", chunk["metadata"]["source_file"], " | ", chunk["text"][:80])
