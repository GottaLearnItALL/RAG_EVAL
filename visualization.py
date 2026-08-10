import chromadb
import numpy as np
import plotly.graph_objects as go 
from sklearn.manifold import TSNE

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("aws_docs")

data = collection.get(include=["embeddings","metadatas"])
embeddings = np.array(data['embeddings'])
tsne = TSNE(n_components=2, random_state = 42) 
reduced_vectors = tsne.fit_transform(embeddings)

services = [m["service"] for m in data["metadatas"]]
palette = {"dynamodb": "#e74c3c", "lambda": "#3498db", "s3": "#2ecc71"}
colors = [palette.get(s, "#999999") for s in services]

fig = go.Figure()

all_files = [m["source_file"] for m in data["metadatas"]]

for svc, color in palette.items():
    mask = np.array([s == svc for s in services])
    pts = reduced_vectors[mask]
    labels = [f for f, m in zip(all_files, mask) if m]   # same mask on the labels
    fig.add_trace(go.Scatter(
        x=pts[:, 0], y=pts[:, 1], mode="markers", name=svc,
        marker=dict(size=5, color=color, opacity=0.8),
        text=labels,
        hoverinfo="text",
    ))                                                    # everything inside Scatter now



fig.update_layout(title='2D Chroma Vector Store Visualization', 
xaxis_title='x', yaxis_title='y',
width=800,
height=600,
margin=dict(r=10, b=10, l=10, t=40))

fig.show()


