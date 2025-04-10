# 🔍 Semantic Search over 5G Technical Specifications

This project implements a semantic search engine and knowledge graph built from 5G technical specification texts. It allows users to input natural language queries and receive contextually relevant sentences from technical documents — powered by sentence embeddings, spaCy NLP, and Streamlit.

---

## ✨ Features

- ⚡ **Semantic Search** using `sentence-transformers`
- 🧠 **Knowledge Graph** generation with entity recognition
- 🔤 Interactive **Streamlit App**
- 📦 Clean project structure with modular code
- 🧪 Toy-scale setup for experimentation and demonstration

---

## 📁 Project Structure

```
semantic-search-5g/
├── data/                      # Raw dataset (CSV format)
│   └── 5GSC.csv
├── embeddings/                # Precomputed sentence embeddings
│   └── 5gsc_semantic_search.pt
├── src/                       # Source code
│   ├── generate_embeddings.py   # Embeds all sentences
│   ├── search.py                # Semantic search logic
│   └── build_knowledge_graph.py # Entity-based knowledge graph
├── app.py                    # Streamlit UI for search
├── environment.yml           # Conda environment setup
├── graph.html                # HTML visualization of the knowledge graph
└── README.md                 # You are here!
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/semantic-search-5g.git
cd semantic-search-5g
```

### 2. Create and activate environment
```bash
conda env create -f environment.yml
conda activate semantic-search-5g
python -m spacy download en_core_web_sm  # Required for entity recognition
```

### 3. Generate sentence embeddings
```bash
python src/generate_embeddings.py
```

### 4. Run the semantic search app
```bash
streamlit run app.py
```

### 5. Generate knowledge graph
```bash
python src/build_knowledge_graph.py
# This creates an interactive graph saved to graph.html
```

Open `graph.html` in your browser to see the extracted entity relationships.

---

## 🔍 Example Search Queries

- "How does 5G manage data tunneling?"
- "What is the role of PDCP in RAN?"
- "Which layers handle user equipment handover?"

---

## 🧪 Dataset

The project uses a curated dataset of 5G technical sentences. See `data/5GSC.csv`.

---

## 🛠️ Built With

- [Sentence Transformers](https://www.sbert.net/)
- [spaCy](https://spacy.io/)
- [NetworkX](https://networkx.org/)
- [PyVis](https://pyvis.readthedocs.io/)
- [Streamlit](https://streamlit.io/)

---