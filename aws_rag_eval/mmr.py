import numpy as np


def mmr(query_emb, chunk_embs, chunks, k=5, lam=0.5):
    selected = []
    candidates = list(range(len(chunks)))

    while len(selected) < k and candidates:
        best_idx, best_score = None, -np.inf
        for i in candidates:
            relevance = np.dot(query_emb, chunk_embs[i])

            if selected:
                redundancy = max(np.dot(chunk_embs[i], chunk_embs[j]) for j in selected)
            else:
                redundancy = 0

            score = lam * relevance - (1 - lam) * redundancy

            if score > best_score:
                best_score, best_idx = score, i

        selected.append(best_idx)
        candidates.remove(best_idx)
    return [chunks[i] for i in selected]
