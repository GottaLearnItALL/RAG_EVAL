def rrf(dense_hits, sparse_hits, k=60, top_n=5):
    scores = {} # Dict stores the score per chunk id.
    lookup = {} # Maps ids to chunks to return full chunk data.

    for hits in dense_hits, sparse_hits:
        for rank,chunk in enumerate(hits):

            # rank is the positionm of the chunk
            # chunk is the chunk of that list
            cid = chunk["id"]
            scores[cid] = scores.get(cid,0) + 1 / (k+rank)
            lookup[cid] = chunk
        
    ranked_id = sorted(scores, key=scores.get, reverse=True)
    
    return [lookup[id] for id in ranked_id[:top_n]]


if __name__ == "__main__":
    # print(bm25_search("test", k=1)[0]["id"])
    # print(retrieve("test", k=1)[0]["id"])
    pass

