import json
from pathlib import Path
import re

CORPUS_DIR = Path('corpus')

# Loads the md files and stores them in a dict with key being the filename

def load_metadata()->dict:
    records = json.loads(Path('corpus/metadata.json').read_text())
    return {record['file']:record for record in records}


# Splits the texts into section by the delimeter # 
def split_on_headings(text: str) -> list[str]:
    pieces = re.split(r'\n(?=#)',text)
    split_text = [piece.strip() for piece in pieces if piece.strip()]
    return split_text

def char_split(section:str, chunk_size: int, overlap:int) -> list[str]:
    if len(section) < chunk_size:
        return [section]
    
    pieces = []
    start = 0
    
    while start < len(section):
        pieces.append(section[start : start+chunk_size])
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
                        "service": record['service'],
                        "title": record['title'],
                        "url": record["url"],
                        "source_file": filename,
                    },
                }
                chunks.append(chunk)
    return chunks



if __name__ == '__main__':
    chunks = build_chunks()
    print(len(chunks))
    for c in chunks[:3]:
        print(c["id"], " | ", c["metadata"]["source_file"], " | ", c["text"][:80])