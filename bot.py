import json
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load intents
with open("intents.json", "r") as f:
    data = json.load(f)

lemmatizer = WordNetLemmatizer()
