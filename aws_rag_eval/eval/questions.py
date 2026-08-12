import json

from aws_rag_eval.paths import EVAL_PATH


def load_questions() -> list[dict]:
    return json.loads(EVAL_PATH.read_text(encoding="utf-8"))
