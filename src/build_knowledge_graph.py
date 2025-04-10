import pandas as pd
import spacy
import networkx as nx
from pyvis.network import Network

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load the data
df = pd.read_csv("data/5GSC.csv")
texts = df["text"].tolist()

# Limit for simplicity (you can increase later)
texts = texts[:100]

# Create graph
G = nx.DiGraph()

for text in texts:
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ in ("ORG", "PRODUCT", "GPE", "TECHNOLOGY", "NORP")]
    if len(entities) >= 2:
        for i in range(len(entities) - 1):
            G.add_edge(entities[i], entities[i + 1])

# Visualize with pyvis
net = Network(notebook=False)
net.from_nx(G)
net.write_html("graph.html")
print("✅ Graph saved to graph.html. Open it manually in a browser.")