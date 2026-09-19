from rank_bm25 import BM25Okapi
from aws_rag_eval.chunker import build_chunks

import re

chunks = build_chunks()
tokenized = [c['text'].lower().split() for c in chunks]
bm25 = BM25Okapi(tokenized)


def tokenize(text):
    return re.findall(r"[a-z0-9_\-\.]+", text.lower())

tokenized = [tokenize(c["text"]) for c in chunks]
bm25 = BM25Okapi(tokenized)


def bm25_search(question, k=20):
    scores = bm25.get_scores(tokenize(question))
    top_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]

    return [
        {
            "id": chunks[i]["id"],
            "text": chunks[i]["text"],
            "metadata": chunks[i]["metadata"],
            "bm25_score": float(scores[i]),
        }
        for i in top_idx
    ]


if __name__ == '__main__':
    for q in ["What is x-amazon-apigateway-integration used for?",
          "I'm seeing a 502 Bad Gateway from my Lambda integration"]:
        print(q)
        for h in bm25_search(q,k=3):
            print("  ", round(h["bm25_score"], 2), h["metadata"]["source_file"])

