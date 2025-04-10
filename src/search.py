import torch
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load saved data
data = torch.load("embeddings/5gsc_semantic_search.pt")
texts = data["texts"]
embeddings = data["embeddings"]

def search(query, top_k=5):
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Compute cosine similarities
    scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]

    # Get top results
    top_results = torch.topk(scores, k=top_k)

    # Return matches
    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        results.append({
            "text": texts[idx],
            "score": float(score)
        })

    return results