import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_messages(file):
    df = pd.read_csv(file, encoding="utf-8")
    messages = []

    for col in df.columns:
        for val in df[col]:
            if pd.notna(val):
                parts = str(val).split("\n")
                for p in parts:
                    p = p.strip()
                    if p != "":
                        messages.append(p)

    return messages


def detect_topics(messages, threshold=0.22, min_topic_size=8):
    vectorizer = TfidfVectorizer()
    topics = []
    current_topic = [messages[0]]

    for i in range(1, len(messages)):
        msg = messages[i].strip()

        if len(msg.split()) < 4:
            current_topic.append(msg)
            continue

        context = " ".join(current_topic[-8:])

        try:
            vectors = vectorizer.fit_transform([context, msg])
            sim = cosine_similarity(vectors[0], vectors[1])[0][0]
        except:
            sim = 1.0

        if sim < threshold and len(current_topic) >= min_topic_size:
            topics.append(current_topic)
            current_topic = []

        current_topic.append(msg)

    topics.append(current_topic)
    return topics


def summarize_topic(topic):
    lines = sorted(topic, key=lambda x: len(x), reverse=True)
    return " ".join(lines[:3])


def hundred_message_checkpoints(messages):
    checkpoints = []

    for i in range(0, len(messages), 100):
        chunk = messages[i:i+100]
        summary = summarize_topic(chunk)

        checkpoints.append({
            "start": i,
            "end": i + len(chunk),
            "summary": summary
        })

    return checkpoints


if __name__ == "__main__":
    msgs = load_messages("conversations.csv")
    print("Total messages:", len(msgs))

    topics = detect_topics(msgs[:300])
    print("Total topics:", len(topics))

    for i, t in enumerate(topics[:3]):
        print(f"\nTopic {i+1}:")
        for line in t[:3]:
            print(line)

    for i, t in enumerate(topics[:3]):
        print(f"\nSummary {i+1}:")
        print(summarize_topic(t))

    checkpoints = hundred_message_checkpoints(msgs[:300])

    for c in checkpoints[:3]:
        print(f"\nMessages {c['start']} - {c['end']}")
        print(c["summary"])