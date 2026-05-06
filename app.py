import streamlit as st
from rag import load_messages, detect_topics, summarize_topic
from persona import build_persona
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

msgs = load_messages("conversations.csv")
topics = detect_topics(msgs[:500])
summaries = [summarize_topic(t) for t in topics]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(summaries)

persona = build_persona(msgs[:500])

def retrieve(query, k=2):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, vectors)[0]
    idxs = sims.argsort()[-k:][::-1]
    return [summaries[i] for i in idxs]

st.title("Conversation RAG Chatbot")

q = st.text_input("Ask something")

if q:
    q = q.lower()

    if "habit" in q:
        st.write(persona["habits"])

    elif "person" in q or "describe" in q:
        st.write(persona["personality"])

    elif "talk" in q or "style" in q:
        st.write(persona["communication_style"])

    else:
        results = retrieve(q)
        for r in results:
            st.write(r)