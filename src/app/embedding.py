import json
import os

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDINGS_DIR = "data/embeddings"
INDEX_FILE = os.path.join(EMBEDDINGS_DIR, "index.faiss")
DOCS_FILE = os.path.join(EMBEDDINGS_DIR, "docs.json")
MODEL_NAME = "all-MiniLM-L6-v2"


def chunk_record(record):
    """Chunk a JSON record into individual field-level chunks and a full summary chunk."""
    chunks = []
    name = record.get("restaurant_name", "Unknown")

    # One chunk per field with the restaurant name as context
    for key, value in record.items():
        chunks.append(f"{name} - {key}: {value}")

    # One full summary chunk combining all fields
    summary = " | ".join(f"{k}: {v}" for k, v in record.items())
    chunks.append(summary)

    return chunks


def init_vectorstore(file_path="data/raw/data.json"):
    """Load documents, chunk each record, embed, and save the FAISS index to data/embeddings."""
    with open(file_path, "r") as f:
        data = json.load(f)

    all_chunks = []
    for item in data:
        if isinstance(item, dict):
            all_chunks.extend(chunk_record(item))
        else:
            all_chunks.append(str(item))

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(all_chunks, show_progress_bar=True)
    embeddings = np.array(embeddings, dtype="float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
    faiss.write_index(index, INDEX_FILE)
    with open(DOCS_FILE, "w") as f:
        json.dump(all_chunks, f)

    return index, all_chunks


def load_vectorstore():
    """Load a previously saved FAISS index and docs from data/embeddings."""
    index = faiss.read_index(INDEX_FILE)
    with open(DOCS_FILE, "r") as f:
        docs = json.load(f)
    return index, docs


def search(query, k=5):
    """Search the vector store for the top-k most similar documents."""
    index, docs = load_vectorstore()
    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query], show_progress_bar=False)
    query_embedding = np.array(query_embedding, dtype="float32")
    distances, indices = index.search(query_embedding, k)
    return [(docs[i], distances[0][j]) for j, i in enumerate(indices[0]) if i < len(docs)]


if __name__ == "__main__":
    index, docs = init_vectorstore()
    print(f"Vector store initialized and saved to {EMBEDDINGS_DIR} with {index.ntotal} vectors.")
