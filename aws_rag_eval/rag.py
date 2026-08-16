from anthropic import Anthropic

from aws_rag_eval.retrieve import retrieve
from aws_rag_eval.query_rewriting import rewrite_query

client = Anthropic()


def build_prompt(question, chunks):
    context = "\n\n---\n\n".join(c["text"] for c in chunks)
    return f"""Answer using ONLY the context below . If the answer isn't in the context, say 'Not in the provided documentation.'

    Context: {context}
    Question: {question}
    """


def answer(question) -> tuple[str, list[dict]]:
    rewritten = rewrite_query(question)
    chunks = retrieve(rewritten, k=5)
    prompt = build_prompt(question, chunks)
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip(), chunks, rewritten


if __name__ == "__main__":
    for q in [
        "How do I add a secondary index to an existing table?",
        "What is the exact price of a DynamoDB write?",
    ]:
        a, _ = answer(q)
        print(q, "\n→", a, "\n")
