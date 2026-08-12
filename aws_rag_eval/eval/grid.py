from aws_rag_eval.eval.recall import evaluate_precision, evaluate_recall

configs = {
    "baseline": dict(),
    "rerank": dict(rerank_on=True),
    "rewrite": dict(rewrite_on=True),
    "mmr": dict(mmr_on=True),
}


def main() -> None:
    print(f"{'config':10} {'recall':>8} {'precision':>10}")

    for name, flags in configs.items():
        r = evaluate_recall(k=5, **flags)["recall"]
        p = evaluate_precision(k=5, **flags)
        print(f"{name:10} {r:>8.2f} {p:>10.2f}")


if __name__ == "__main__":
    main()
