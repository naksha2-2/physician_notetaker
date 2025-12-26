📌 Overview

Physician Notetaker is a prototype NLP-based system that extracts structured clinical information from doctor–patient conversation transcripts.
It assists in medical documentation by identifying symptoms, diagnosis, treatments, patient sentiment, intent, and (as a bonus) generating structured SOAP notes.
This project is intended for documentation support and learning purposes only, not for clinical decision-making.

🧠 Features
1. Clinical Information Extraction

Named Entity Recognition and sentence parsing using spaCy

Rule-based extraction of:

Symptoms

Diagnosis

Treatment

Prognosis

2. Sentiment & Intent Analysis

Transformer-based sentiment analysis (DistilBERT)

Rule-based intent detection to identify:

Symptom reporting

Seeking reassurance

Acceptance / follow-up

3. SOAP Note Generation

A SOAP note is a standardized clinical documentation format consisting of:

Subjective

Objective

Assessment

Plan

This project includes a basic automated SOAP note generator that structures extracted clinical data into a readable SOAP note using logical rule-based mapping.

📍 Sample Input (Transcript)
Doctor: How are you feeling today?
Patient: I had a car accident. My neck and back hurt a lot for four weeks.
Doctor: Did you receive treatment?
Patient: Yes, I had ten physiotherapy sessions, and now I only have occasional back pain.

📍 Generated SOAP Note (Output)

Subjective:
Patient reports neck and back pain following a car accident, lasting approximately four weeks. Currently experiences occasional discomfort.

Objective:
Patient has completed ten physiotherapy sessions and has taken painkillers.

Assessment:
Findings are consistent with musculoskeletal injury following a motor vehicle accident, showing improvement after treatment.

Plan:
Continue monitoring symptoms. Follow-up is recommended if pain persists or worsens.

🧩 Project Structure
physician_notetaker/
│
├── nlp.py               # NLP extraction, sentiment & intent analysis
├── soap_generator.py    # SOAP note generation logic (bonus)
├── app.py               # Optional runner script
├── requirements.txt
└── README.md

🚀 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

2️⃣ Run the application
python app.py

🧪 Development Environment

Developed and tested using Google Colab

Converted into modular Python files for reproducibility
