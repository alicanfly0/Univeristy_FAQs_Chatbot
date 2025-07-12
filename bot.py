import json
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load intents
with open("intents.json", "r") as f:
    data = json.load(f)

lemmatizer = WordNetLemmatizer()

# Map key tokens to (intent_tag, url_fragment)
synonyms_map = {
    "admission": ("application_process", "application-process"),
    "admissions": ("application_process", "application-process"),
    "application": ("application_process", "application-process"),
    "process": ("application_process", "application-process"),
    "deadline": ("application_deadline", "application-deadline"),
    "documents": ("documents_required", "documents-required"),
    "document": ("documents_required", "documents-required"),
    "tuition": ("tuition_fees", "tuition-fees"),
    "fee": ("tuition_fees", "tuition-fees"),
    "fees": ("tuition_fees", "tuition-fees"),
    "scholarship": ("scholarships", "scholarships"),
    "aid": ("financial_aid", "financial-aid"),
    "tour": ("campus_tour", "campus-tour"),
    "library": ("library_hours", "library-hours"),
    "parking": ("parking", "parking"),
    "housing": ("housing", "housing"),
    "dining": ("dining", "dining"),
    "tech": ("tech_support", "tech-support"),
    "support": ("tech_support", "tech-support"),
    "exam": ("exam_schedule", "exam-schedule"),
    "transcript": ("transcript_request", "transcript-request"),
}


def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

