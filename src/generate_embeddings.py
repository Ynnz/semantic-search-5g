import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

# Load the dataset
df = pd.read_csv("data/5GSC.csv")
texts = df["text"].tolist()

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print("📡 Generating embeddings...")
embeddings = model.encode(texts, convert_to_tensor=True)

# Save embeddings + texts
output = {
    "texts": texts,
    "embeddings": embeddings
}
torch.save(output, "embeddings/5gsc_semantic_search.pt")

print("✅ Embeddings saved to embeddings/5gsc_semantic_search.pt")