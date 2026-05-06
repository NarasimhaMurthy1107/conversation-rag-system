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


while True:
    q = input("\nAsk: ").lower()

    if "habit" in q:
        print(persona["habits"])

    elif any(x in q for x in ["person", "describe", "personality"]):
        print(persona["personality"])

    elif any(x in q for x in ["talk", "style", "communicate"]):
        print(persona["communication_style"])

    else:
        results = retrieve(q, k=2)
        for i, r in enumerate(results, 1):
            print(f"\nResult {i}:\n{r}")