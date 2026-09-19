import chromadb
import numpy as np
import plotly.graph_objects as go
from sklearn.manifold import TSNE

# from aws_rag_eval.paths import CHROMA_PATH

# client = chromadb.PersistentClient(path=str(CHROMA_PATH))
# collection = client.get_collection("aws_docs")

# data = collection.get(include=["embeddings", "metadatas"])
# embeddings = np.array(data["embeddings"])
# tsne = TSNE(n_components=2, random_state=42)
# reduced_vectors = tsne.fit_transform(embeddings)

# services = [m["service"] for m in data["metadatas"]]
# palette = {"dynamodb": "#e74c3c", "lambda": "#3498db", "s3": "#2ecc71"}

# fig = go.Figure()
# all_files = [m["source_file"] for m in data["metadatas"]]

# for svc, color in palette.items():
#     mask = np.array([s == svc for s in services])
#     pts = reduced_vectors[mask]
#     labels = [f for f, m in zip(all_files, mask) if m]
#     fig.add_trace(
#         go.Scatter(
#             x=pts[:, 0],
#             y=pts[:, 1],
#             mode="markers",
#             name=svc,
#             marker=dict(size=5, color=color, opacity=0.8),
#             text=labels,
#             hoverinfo="text",
#         )
#     )

# fig.update_layout(
#     title="2D Chroma Vector Store Visualization",
#     xaxis_title="x",
#     yaxis_title="y",
#     width=800,
#     height=600,
#     margin=dict(r=10, b=10, l=10, t=40),
# )

# fig.show()
import matplotlib.pyplot as plt
import numpy as np

configs    = ["baseline", "rerank", "rewrite", "mmr"]
recall     = [0.85, 0.85, 0.95, 0.70]
precision  = [0.41, 0.41, 0.58, 0.28]

x = np.arange(len(configs))
width = 0.38

fig, ax = plt.subplots(figsize=(10, 6), dpi=200)

b1 = ax.bar(x - width/2, recall,    width, label="Context recall",    color="#2563eb")
b2 = ax.bar(x + width/2, precision, width, label="Context precision", color="#93c5fd")

# value labels on top of each bar
for bars in (b1, b2):
    ax.bar_label(bars, fmt="%.2f", padding=3, fontsize=12)

ax.set_ylim(0, 1.05)
ax.set_ylabel("Score", fontsize=14)
ax.set_title("RAG retrieval: 4 configs vs. hand-verified ground truth",
             fontsize=16, weight="bold", pad=14)
ax.set_xticks(x)
ax.set_xticklabels(configs, fontsize=13)
ax.tick_params(axis="y", labelsize=12)
ax.legend(fontsize=12, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("rag_eval.png", bbox_inches="tight")
plt.show()