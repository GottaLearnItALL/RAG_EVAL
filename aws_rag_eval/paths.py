from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = PROJECT_ROOT / "corpus"
EVAL_PATH = PROJECT_ROOT / "data" / "eval.json"
CHROMA_PATH = PROJECT_ROOT / "chroma_db"
