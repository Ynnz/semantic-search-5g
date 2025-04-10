import torch

# Load the file
data = torch.load("embeddings/5gsc_semantic_search.pt")

# View keys
print("Keys:", data.keys())

# Preview content
print("\nSample sentence:")
print(data["texts"][0])

print("\nEmbedding vector (first 5 values):")
print(data["embeddings"][0][:5])