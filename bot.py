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


def get_response(user_input):
    tokens = preprocess(user_input)

    # 1. Check synonyms map for direct keyword
    for tok in tokens:
        if tok in synonyms_map:
            tag, url_frag = synonyms_map[tok]
            # Check if JSON has this intent
            intent = next((i for i in data["intents"] if i["tag"] == tag), None)
            if intent:
                return random.choice(intent["responses"])
            # Dynamic fallback if JSON missing
            return f"For information on {tok}, please visit https://example.com/{url_frag}"


    # 2. Bag-of-words match
    best_intent = None
    best_score = 0
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pat_tokens = preprocess(pattern)
            score = sum(1 for pt in pat_tokens if pt in tokens)
            if score > best_score:
                best_score = score
                best_intent = intent

    if best_intent and best_score > 0:
        return random.choice(best_intent["responses"])

