readme file 
# Physician Notetaker

# Overview
This project extracts structured clinical information from doctor and patient conversations using NLP techniques.So this is basically creates an pipeline.Here the goal is to convert unstructured medical text into a concise, structured summary suitable for clinical documentation.

#Approach

spaCy                                         for basic NER and sentence parsing
Rule-based keyword matching                   for symptoms, diagnosis, treatment
KeyBERT                                       for keyword extraction
Transformer-based sentiment analysis          for patient emotional state
Rule-based intent detection

#How to Run

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py

#Assumptions
 Input text is English
 Patient name is predefined for demo
 Rule-based medical extraction for simplicity

#Limitations
 here medical-specific NER models are not used
 Rule-based matching may miss synonyms

#Future Improvements
using clinical NER models like scispaCy medical models
 we can add speech-to-text integration





