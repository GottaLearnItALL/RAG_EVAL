import anthropic

from aws_rag_eval.eval.questions import load_questions

client = anthropic.Anthropic()


def rewrite_query(question) -> str:
    prompt = f"""Rewrite this question as a search query using formal AWS documentation terminoly,
        Output ONLY the rewritten query, no explanation.

        Example:
        Question: how do I make my table survive a crash?
        Query: how to enable DynamoDB backup and restore for a table


        Question: {question}
        Query:"""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


if __name__ == "__main__":
    questions = load_questions()
    for qid in [1, 14]:
        q = [x for x in questions if x["id"] == qid][0]
        print("ORIG:", q["question"])
        print("NEW :", rewrite_query(q["question"]))
        print()
