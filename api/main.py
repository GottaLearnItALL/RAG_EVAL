from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import sys
import os
import json, datetime
import uuid
from pathlib import Path
import boto3

s3 = boto3.client("s3")
BUCKET = "aryan-rag-logs"


HTML_PATH = Path(__file__).parent / "index.html"

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
    
    record = {
            "query_id": query_id,
            "ts": datetime.datetime.now().isoformat(),
            "question":q.question,
            "sources": [c['metadata']['source_file'] for c in chunks],
            "distances": [c['distance'] for c in chunks],
            "rewrite":rewritten,
            "answer":text,
        }
    key = f"logs/{datetime.date.today()}/{query_id}.json"

    try:
        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=json.dumps(record),
            ContentType="application/json",
        )
    except Exception as e:
        print(f"S3 log failed: {e}")   # visible in Render logs

    return {
        "query_id":query_id,
        "answer": text,
        "sources": [c['metadata']['source_file'] for c in chunks],
        "rewrite": rewritten
    }

@app.get("/")
def home():
    return FileResponse(HTML_PATH)


@app.post("/feedback")
def feedback(f: Feedback):
    record = {
        "ts": datetime.datetime.now().isoformat(),
        "query_id": f.query_id,
        "verdict": f.verdict,
    }
    key = f"feedback/{datetime.date.today()}/{f.query_id}.json"
    try:
        s3.put_object(
            Bucket=BUCKET, 
            Key=key, Body=json.dumps(record),
            ContentType="application/json")
    except Exception as e:
        print(f"S3 feedback log failed: {e}")

    return {"ok": True}

