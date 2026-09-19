import json

from aws_rag_eval.paths import EVAL_PATH, EVAL_PATH_HARD


def load_questions() -> list[dict]:
    return json.loads(EVAL_PATH.read_text(encoding="utf-8"))



def load_hard_questions() -> list[dict]:
    return json.loads(EVAL_PATH_HARD.read_text(encoding='utf-8'))
    
