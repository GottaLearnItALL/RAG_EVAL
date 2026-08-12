# AWS Docs RAG — From-Scratch Retrieval + Evaluation Harness

A retrieval-augmented generation (RAG) system built over AWS developer
documentation (DynamoDB, Lambda, S3), with a hand-written evaluation harness
that measures retrieval quality, generation quality, and the effect of four
different retrieval techniques. No LangChain — every stage is written from
scratch so the behavior is fully understood and measurable.

The point of this project is **not** "a RAG demo." It's the eval harness and
the failure analysis: measuring *which* techniques help, *which* don't, and
*why*.

---

## What RAG is

**RAG (Retrieval-Augmented Generation)** = instead of letting an LLM answer
from memory (where it can hallucinate), you first *retrieve* relevant documents,
then *give them to the LLM* and instruct it to answer only from those. Two
stages, and they fail for different reasons:

- **Retrieval** — fetch the right chunks. If the answer isn't in what you
  fetched, generation is doomed.
- **Generation** — given the chunks, write a faithful answer.

Keeping these separate is the core of the whole project — it turns "the RAG is
bad" (useless) into "retrieval recall is 0.95, generation faithfulness is 1.0"
(actionable).

---

## The pipeline (stages, in order)

1. **Chunk** — cut the 44 doc pages into small, findable pieces.
   Split on markdown headings first (coherent topics), then slice any
   oversized section into fixed-size character windows with overlap so a
   sentence isn't severed at a boundary. → 1214 chunks (size 500, overlap 50).
2. **Embed + Store** — each chunk is turned into a vector (an
   **embedding** = a list of numbers positioning the text in "meaning space,"
   where similar meaning = nearby position). Stored in **Chroma** (a local
   vector database) using its built-in all-MiniLM embedding model.
3. **Retrieve** — embed the question into the same space, return the *k*
   chunks whose vectors are closest.
4. **Generate** — stuff retrieved chunks into a prompt that says "answer ONLY
   from this context," send to an LLM (Claude), get a grounded answer.

---

## Key concepts (with definitions)

**Embedding** — a numeric vector representing a piece of text's meaning. Texts
with similar meaning get nearby vectors. This is what makes "search by meaning"
possible: "bolt on an index" and "add a global secondary index" *should* land
near each other (and when they don't, that's a bug you can measure — see Query
Rewriting).

**Bi-encoder** — the embedding model used for fast retrieval. Question and
chunk are embedded *separately*, then compared by distance. Fast (embed the
corpus once), but because the two texts never meet, it can't reason about how
they relate — it matches on shared vocabulary.

**Cross-encoder (reranking)** — a slower model that reads question and chunk
*together* and outputs one relevance score. Used in a two-stage pattern:
bi-encoder casts a wide net (top 20), cross-encoder re-scores just those 20 and
keeps the best 5. Fixes *ranking* failures (right doc retrieved but ranked too
low).

**MMR (Maximal Marginal Relevance)** — a retrieval strategy that balances
relevance to the query against *diversity* (avoiding near-duplicate chunks). It
picks chunks that are relevant but different from each other. Helps when an
answer is spread across multiple documents; hurts when each answer lives in a
single document (as here).

**Query Rewriting** — an LLM rewrites the user's casual question into formal
documentation vocabulary *before* embedding. Fixes *vocabulary-mismatch*
failures, where the question and the answer doc use different words for the
same thing.

**LLM-as-judge** — using a second LLM call to *score* the first LLM's output.
Used for evaluation criteria that need judgment (like faithfulness) rather than
an exact-match check. The craft is forcing structured (JSON) output so scores
are countable, and validating the judge against known good/bad cases before
trusting it.

---

## The metrics (the rulers)

RAG is evaluated on two sides. This project built one to two metrics per side.

### Retrieval metrics

**Context Recall** — of the documents needed to answer, how many did retrieval
fetch? Here it's a pure-Python check: each eval question is labeled with the
`source_file` its answer lives in; recall asks "was a chunk from that file among
the retrieved chunks?" No LLM, no fuzziness — bedrock metric.

**Context Precision** — of the chunks retrieved, how many were relevant?
(relevant = from the labeled source file). Recall catches *misses*; precision
catches *noise*.

### Generation metric

**Faithfulness** — is every claim in the LLM's answer supported by the
retrieved chunks, or did it invent something? Measured with LLM-as-judge
(binary 0/1). A strict "answer only from context" generation prompt is what
makes this measurable — without it, the model answers from training knowledge
and hallucinations are invisible.

*(Not built, but part of the full picture: MRR/hit-rate for rank position,
and Answer Relevancy for whether the answer addresses the question.)*

---

## The ground-truth eval set

20 question/answer pairs, each labeled with the `source_file` its answer comes
from. Written in a casual "confused student" voice to stress-test retrieval
against real phrasing. **Every label was hand-verified** — the answer actually
appears in its named file. This verification is what makes the recall metric
*true* rather than vibes; a wrong label produces a fake "miss" that sends you
chasing a bug that doesn't exist (this happened — see Q10 below).

---

## Results

### Baseline and the failure analysis

Baseline retrieval scored **recall@5 = 0.85** (17/20). The three misses were
each traced individually — and they had *three different root causes*:

- **Q1** — vocabulary mismatch. The answer chunk existed and was correctly
  labeled, but the casual question ("bolt on an index") and the doc's formal
  wording ("global secondary index") embedded too far apart, so the answer chunk
  was never even retrieved.
- **Q10** — a *mislabeled* ground-truth entry (pointed at the wrong file).
  Fixed the label. This was a broken test, not a retrieval failure.
- **Q14** — vocabulary mismatch again. The question asked about "invoking"
  Lambda; the answer was about "resource-based policies / permissions." Different
  words, same concept — the correct doc was never retrieved.

Reading each miss (not just the aggregate score) is what separated "the RAG is
bad" from a precise, per-failure diagnosis.

### Technique comparison grid

Each retrieval technique was measured individually against baseline:

| Config    | Recall | Precision |
|-----------|:------:|:---------:|
| baseline  |  0.85  |   0.41    |
| rerank    |  0.85  |   0.41    |
| rewrite   |  0.95  |   0.58    |
| mmr       |  0.70  |   0.28    |

### What the grid shows

- **Query rewriting is the decisive win** (+10 recall, +17 precision). It
  addressed the *actual* root cause — vocabulary mismatch — fixing both Q1 and
  Q14 without breaking anything.
- **Reranking was neutral** (moved nothing). Its job is fixing *ranking*
  failures, but the misses here weren't ranking failures — the correct docs were
  never retrieved in the first place. Reranking can only re-order what was
  fetched; it can't recover a doc that isn't in the pool.
- **MMR was net-negative** on these metrics. Its diversity objective conflicts
  with single-source ground truth (each answer lives in one file), so it traded
  away the correct doc for variety. MMR is the wrong tool for single-source QA.

**The core insight:** RAG interventions have a dependency order
(chunking → retrieval → reranking), and a downstream fix can't repair an
upstream failure. Matching the technique to the *specific failure mode* mattered
far more than stacking techniques.

### Generation

Faithfulness reached **1.0** after fixing a judge false-positive (the judge was
initially penalizing correct "not in the documentation" refusals as
hallucinations — refusing to answer isn't a hallucination).

**Known limitations (honest notes):**
- LLM-as-judge is **non-deterministic** — the same harness gave the same score
  but a *different* set of flagged questions run-to-run. A production version
  would run it 3× and average, or set temperature=0.
- A faithfulness of 1.0 may mean the metric is too lenient to discriminate.
  Harder, adversarial questions would stress-test it better.
- The precision metric uses strict exact-file matching — a chunk from a related
  file might be genuinely useful but scores 0.

---

## Stack

- **Vector DB:** Chroma (local, persistent) with built-in all-MiniLM embeddings
- **Reranker:** `cross-encoder/ms-marco-MiniLM-L-6-v2` (sentence-transformers)
- **Generation + query rewriting + judge:** Claude (Anthropic API)
- **Everything else** (chunking, retrieval logic, MMR, all metrics, the harness):
  hand-written Python, no LangChain

## Project layout

```
AWS_RAG_EVAL/
├── aws_rag_eval/          # Python package
│   ├── chunker.py         # heading + character-window chunking
│   ├── ingest.py          # embed + store into Chroma
│   ├── retrieve.py        # retrieval (rerank / rewrite / mmr flags)
│   ├── rerank.py          # cross-encoder reranking
│   ├── query_rewriting.py # LLM query rewriter
│   ├── mmr.py             # Maximal Marginal Relevance
│   ├── rag.py             # retrieve → prompt → Claude generation
│   ├── faithfulness.py    # LLM-as-judge faithfulness scoring
│   ├── visualization.py   # t-SNE plot of the embedding space
│   └── eval/
│       ├── recall.py      # recall + precision harness
│       └── grid.py        # technique comparison grid
├── corpus/                # AWS doc pages (markdown)
├── data/
│   └── eval.json          # 20 hand-verified ground-truth Q/A pairs
├── scripts/
│   └── grab_corpus.py     # download corpus from AWS docs
└── chroma_db/             # local vector store (gitignored)
```

## Quick start

```bash
uv sync

# Ingest corpus into Chroma
uv run python -m aws_rag_eval.ingest

# Run retrieval eval grid
uv run python -m aws_rag_eval.eval.grid

# Run recall/precision only
uv run python -m aws_rag_eval.eval.recall

# Refresh corpus from AWS docs
uv run python scripts/grab_corpus.py
```
