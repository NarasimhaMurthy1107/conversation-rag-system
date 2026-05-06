# Conversation RAG System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system on conversational datasets.

The system processes conversations chronologically, detects topic changes, generates summaries, extracts user persona information, and answers user queries using retrieval-based context matching.

---

## Features

- Chronological conversation processing
- Topic change detection
- Topic checkpoint summaries
- 100-message checkpoint summaries
- Persona extraction
- Retrieval-based chatbot
- Streamlit web interface

---

## Topic Change Detection

The system processes messages sequentially and compares each incoming message with recent conversational context.

### Method Used
- TF-IDF vectorization
- Cosine similarity

### Logic
- Each message is compared with a sliding context window of previous messages
- If similarity drops below a threshold, a new topic segment is created
- Very short messages are ignored to reduce noise
- Minimum topic size is enforced to avoid over-fragmentation

This allows the system to split conversations into chronological topic checkpoints instead of treating the entire chat as one topic.

---

## Topic Checkpoints

Whenever a topic change is detected:
- A new topic checkpoint is created
- A summary is generated for that topic segment only

Example:

Topic 1 → messages 1–25  
Topic 2 → messages 26–60  
Topic 3 → messages 61–90

---

## 100-Message Checkpoints

Independent summaries are generated every 100 messages.

Purpose:
- Provide coarse-grained conversation memory
- Improve long conversation tracking

---

## Retrieval System

The chatbot retrieves relevant information using:
- TF-IDF embeddings
- Cosine similarity ranking

### Retrieval Flow
1. User query is vectorized
2. Query is compared against stored topic summaries
3. Top-k most relevant summaries are retrieved
4. Results are returned to the user

This ensures retrieval is context-aware and not random.

---

## Persona Extraction

Persona is built using rule-based signals extracted from conversations.

### Extracted Categories
- Habits
- Personality traits
- Communication style

### Examples
- Student
- Likes cooking
- Positive personality
- Expressive communication style

Persona is derived only from actual conversation signals.

---

## Chatbot

The chatbot supports questions like:
- What kind of person is this user?
- What are their habits?
- How do they talk?
- What do they like cooking?

The chatbot combines:
- Retrieved topic summaries
- Persona information

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## Project Structure

conversation-rag-system/

├── app.py  
├── rag.py  
├── persona.py  
├── chatbot.py  
├── requirements.txt  
├── README.md  
├── conversations.csv  
└── .gitignore

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
