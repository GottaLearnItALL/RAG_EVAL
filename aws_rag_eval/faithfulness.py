import json

import anthropic

from aws_rag_eval.eval.questions import load_questions
from aws_rag_eval.rag import answer

client = anthropic.Anthropic()


def judge_faithfulness(answer, chunks):
    context = "\n\n---\n\n".join(c["text"] for c in chunks)
    prompt = f"""You are evaluating if an answer is faithful to its context.
        An answer is faithful (1) if EVERY claim is supported by the context. If any claim isn't supported, it's unfaithful (0).
        A response that declines to answer because the information is absent from the context is FAITHFUL (score 1) — refusing to answer is not a hallucination.

        Context:
        {context}

        Answer:
        {answer}

        Respond ONLY with JSON: {{"score": 0 or 1, "reason": "brief"}}"""
    resp = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = resp.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.strip("`").removeprefix("json").strip()
    return json.loads(raw)


def main() -> None:
    questions = load_questions()
    scores = []

    for q in questions:
        a, chunks, _ = answer(q["question"])
        verdict = judge_faithfulness(a, chunks)
        scores.append(verdict["score"])
        if verdict["score"] == 0:
            print(q["id"], "UNFAITHFUL:", verdict["reason"][:80])
    print("Faithfulness:", sum(scores) / len(scores))


if __name__ == "__main__":
    main()
