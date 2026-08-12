import chromadb

from aws_rag_eval.chunker import build_chunks
from aws_rag_eval.paths import CHROMA_PATH


def ingest() -> chromadb.Collection:
    chunks = build_chunks()
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))

    try:
        client.delete_collection("aws_docs")
    except Exception:
        pass

    collection = client.get_or_create_collection(name="aws_docs")

    collection.add(
        ids=[c["id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks],
    )
    return collection


def main() -> None:
    collection = ingest()
    print(collection.count())


if __name__ == "__main__":
    main()
