import chromadb
import numpy as np
from chromadb.utils import embedding_functions

from aws_rag_eval.paths import CHROMA_PATH

ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_collection("aws_docs")


def retrieve(
    question,
    k=5,
    service=None,
    rerank_on=False,
    rewrite_on=False,
    mmr_on=False,
    hybrid_on=False,

) -> list[dict]:

    if rewrite_on:
        from aws_rag_eval.query_rewriting import rewrite_query

        question = rewrite_query(question)

    where = {"service": service} if service else None
    fetch_k = 20 if (rerank_on or hybrid_on) else k
    results = collection.query(query_texts=[question], n_results=fetch_k, where=where)
    ids = results['ids'][0]
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]
    hits = []
    for cid, text, meta, dist in zip(ids,docs, metas, dists):
        hits.append({"id": cid, "text": text, "metadata": meta, "distance": dist})

    if hybrid_on:
        from aws_rag_eval.bm25_ import bm25_search
        from aws_rag_eval.rrf import rrf
        return rrf(hits, bm25_search(question, k=20), top_n=k)

    if rerank_on:
        from aws_rag_eval.rerank import rerank

        hits = rerank(question, hits, top_n=k)

    if mmr_on:
        from aws_rag_eval.mmr import mmr
        results = collection.query(
            query_texts=[question],
            n_results=20,
            where=where,
            include=["documents", "metadatas", "distances", "embeddings"],
        )
        query_emb = np.array(ef([question])[0])
        chunk_embs = [np.array(e) for e in results["embeddings"][0]]
        mmr_chunks = [
            {"text": t, "metadata": m, "distance": d}
            for t, m, d in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
        ]
        return mmr(query_emb, chunk_embs, mmr_chunks, k=k)

    return hits


if __name__ == "__main__":
    for hit in retrieve("How do I add a secondary index to an existing table?", k=5, mmr_on=True):
        print(hit["metadata"]["source_file"])
