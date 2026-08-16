from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import sys
import os
import json, datetime
import uuid

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
target_path = os.path.join(project_root, "aws_rag_eval")

sys.path.insert(0, target_path)

from aws_rag_eval.rag import answer

app = FastAPI()


class Query(BaseModel):
    question: str


class Feedback(BaseModel):
    query_id: str
    verdict: str 


@app.post("/ask")
def ask(q:Query):
    query_id = str(uuid.uuid4())
    text, chunks, rewritten = answer(q.question)
    
    with open("query_log.jsonl","a") as f:
        f.write(json.dumps({
            "query_id": query_id,
            "ts": datetime.datetime.now().isoformat(),
            "question":q.question,
            "sources": [c['metadata']['source_file'] for c in chunks],
            "distances": [c['distance'] for c in chunks],
            "rewrite":rewritten,
            "answer":text,
        }) + "\n")

    return {
        "query_id":query_id,
        "answer": text,
        "sources": [c['metadata']['source_file'] for c in chunks],
        "rewrite": rewritten
    }

@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/feedback")
def feedback(f: Feedback):
    with open("feedback.jsonl", "a") as fh:
        fh.write(json.dumps({
            "ts": datetime.datetime.now().isoformat(),
            "query_id": f.query_id,
            "verdict": f.verdict,
        })+ "\n")
    return {"ok": True}

