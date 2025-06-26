import streamlit as st
from src.retriever import get_triples_about
from src.llm_prompt import generate_answer
import pickle

st.set_page_config(page_title="eBay Knowledge Graph Chatbot", layout="centered")
st.title("🤖 eBay Policy Chatbot")


with st.sidebar:
    st.header("🛠️ Settings")
    if st.button("🔄 Reset Chat"):
        st.session_state.clear()
        st.experimental_rerun()


    try:
        with open("kg/graph.gpickle", "rb") as f:
            G = pickle.load(f)
        st.session_state.graph_nodes = list(G.nodes())
        st.markdown(f"📊 Graph Stats:")
        st.markdown(f"- 🧠 Nodes: {len(G.nodes())}")
        st.markdown(f"- 🔗 Relations: {len(G.edges())}")
    except Exception as e:
        st.warning("⚠️ Couldn't load graph stats.")
        st.session_state.graph_nodes = []


if "messages" not in st.session_state:
    st.session_state.messages = []


query = st.chat_input("Ask about eBay terms, policies, or seller rules...")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("Thinking..."):

        matched_entity = None
        for node in st.session_state.graph_nodes:
            if node.lower() in query.lower():
                matched_entity = node
                break

        if matched_entity:
            triples = get_triples_about(matched_entity)
        else:
            triples = []

        if not triples:
            answer = "I'm sorry, I couldn't find relevant information in the knowledge graph."
        else:
            answer = generate_answer(triples, query)


    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})