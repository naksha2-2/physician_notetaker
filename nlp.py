

# !pip install spacy scispacy transformers keybert torch
# !python -m spacy download en_core_web_sm
# !pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/en_core_sci_md-0.5.4.tar.gz



import spacy
import scispacy
import torch
import transformers
import numpy

print("spaCy:", spacy.__version__)
print("scispaCy:", scispacy.__version__)
print("NumPy:", numpy.__version__)
print("Torch:", torch.__version__)

import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

print("spaCy model loaded successfully")

text = """
Patient was involved in a car accident on September 1st.
She hit her head and experienced neck and back pain.
She was diagnosed with whiplash injury.
She took painkillers and completed ten physiotherapy sessions.
Currently she experiences occasional back pain.
Doctor expects full recovery within six months.
"""
doc = nlp(text)

entities = []
for ent in doc.ents:
    entities.append((ent.text, ent.label_))

entities

SYMPTOMS = ["neck pain", "back pain", "head"]
TREATMENTS = ["physiotherapy", "painkillers"]
DIAGNOSIS = ["whiplash"]
PROGNOSIS = ["full recovery"]

summary = {
    "Symptoms": [],
    "Diagnosis": None,
    "Treatment": [],
    "Prognosis": None
}

lower_text = text.lower()

for s in SYMPTOMS:
    if s in lower_text:
        summary["Symptoms"].append(s.title())

for t in TREATMENTS:
    if t in lower_text:
        summary["Treatment"].append(t.title())

for d in DIAGNOSIS:
    if d in lower_text:
        summary["Diagnosis"] = d.title()

for p in PROGNOSIS:
    if p in lower_text:
        summary["Prognosis"] = "Full recovery expected within six months"

summary

from keybert import KeyBERT

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(
    text,
    keyphrase_ngram_range=(1, 3),
    stop_words="english",
    top_n=5
)

keywords

final_report = {
    "Patient_Name": "Janet Jones",
    "Symptoms": summary["Symptoms"],
    "Diagnosis": summary["Diagnosis"],
    "Treatment": summary["Treatment"],
    "Current_Status": "Occasional backache",
    "Prognosis": summary["Prognosis"]
}

final_report

# SENTIMENT ANALYSIS


from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print("Sentiment model loaded")

patient_statements = [
    "I still have some discomfort now and then.",
    "The first four weeks were rough. My neck and back pain were really bad.",
    "It’s nothing like before.",
    "That’s a relief!",
    "That’s great to hear."
]

sentiment_results = sentiment_pipeline(patient_statements)
sentiment_results

def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["pain", "hurt", "discomfort"]):
        return "Symptom Reporting"

    if any(word in text for word in ["worried", "concerned", "affecting"]):
        return "Seeking Reassurance"

    if any(word in text for word in ["relief", "great to hear", "thank you"]):
        return "Reassurance / Acceptance"

    return "General Information"


intent_results = [
    {"text": stmt, "intent": detect_intent(stmt)}
    for stmt in patient_statements
]

intent_results

sentiment_intent_summary = []

for stmt, sent in zip(patient_statements, sentiment_results):
    sentiment_intent_summary.append({
        "statement": stmt,
        "sentiment": sent["label"],
        "confidence": round(sent["score"], 2),
        "intent": detect_intent(stmt)
    })

sentiment_intent_summary