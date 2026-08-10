from chunker import build_chunks
import chromadb
from sklearn.manifold import TSNE
import numpy as np
import plotly.graph_objects as go


chunks = build_chunks()

client = chromadb.PersistentClient(path="chroma_db")

try:
    client.delete_collection("aws_docs")
except Exception:
    pass

collection = client.get_or_create_collection(name='aws_docs')


ids = [c['id'] for c in chunks]
documents = [c['text'] for c in chunks]
metadatas = [c['metadata'] for c in chunks]

collection.add(ids=ids, documents=documents, metadatas=metadatas)


if __name__ == '__main__':
    print(collection.count())