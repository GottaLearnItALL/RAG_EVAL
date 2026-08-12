from aws_rag_eval.eval.questions import load_questions
from aws_rag_eval.retrieve import retrieve


def evaluate_recall(k=5, rerank_on=False, rewrite_on=False, mmr_on=False):
    questions = load_questions()
    hits = 0
    misses = []
    for q in questions:
        retrieved = retrieve(
            q["question"],
            k=k,
            rerank_on=rerank_on,
            rewrite_on=rewrite_on,
            mmr_on=mmr_on,
        )
        retrieved_files = [c["metadata"]["source_file"] for c in retrieved]
        if q["source_file"] in retrieved_files:
            hits += 1
        else:
            misses.append(q["id"])

    recall = hits / len(questions)
    return {"recall": recall, "hits": hits, "total": len(questions), "misses": misses}


def evaluate_precision(k=5, rerank_on=False, rewrite_on=False, mmr_on=False):
    questions = load_questions()
    precisions = []
    for q in questions:
        retrieved = retrieve(
            q["question"],
            k=k,
            rerank_on=rerank_on,
            rewrite_on=rewrite_on,
            mmr_on=mmr_on,
        )
        relevant = sum(
            1 for c in retrieved if c["metadata"]["source_file"] == q["source_file"]
        )
        precisions.append(relevant / len(retrieved))
    return sum(precisions) / len(questions)


def main() -> None:
    print("Baseline recall:", evaluate_recall(k=5))
    print("Baseline precision:", evaluate_precision(k=5))


if __name__ == "__main__":
    main()
