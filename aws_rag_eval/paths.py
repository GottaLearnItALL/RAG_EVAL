from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = PROJECT_ROOT / "corpus"
EVAL_PATH = PROJECT_ROOT / "data" / "eval.json"
EVAL_PATH_HARD = PROJECT_ROOT / "data" / "hard_eval.json"
CHROMA_PATH = PROJECT_ROOT / "chroma_db"
