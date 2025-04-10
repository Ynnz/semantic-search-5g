import streamlit as st
from src.search import search

st.set_page_config(page_title="5G Semantic Search", layout="wide")
st.title("🔍 5G Semantic Search")
st.markdown("Type a question or topic related to 5G technical specifications:")

query = st.text_input("Your query", placeholder="e.g. How does 5G manage data tunneling?")

if query:
    with st.spinner("Searching..."):
        results = search(query, top_k=5)
    st.success(f"Top {len(results)} results:")

    for r in results:
        st.markdown(f"**Score:** {r['score']:.4f}")
        st.write(r['text'])
        st.markdown("---")