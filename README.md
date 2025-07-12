# Rule-Based FAQ Chatbot for Universities

This is a simple yet extensible chatbot built in Python that provides instant answers to frequently asked questions (FAQs) for a university or educational institution. It uses a **rule-based approach** powered by JSON-defined intents and basic NLP techniques such as tokenization, lemmatization, and keyword mapping.

---

## 🚀 Features

* 🔧 **Rule-based architecture** – No machine learning needed
* 🧠 **Natural language preprocessing** – Tokenization and lemmatization using NLTK
* 🔄 **Bag-of-words pattern matching** – Captures phrasing variations
* 🧩 **Synonym mapping** – Recognizes semantically similar questions
* 🎯 **URL-driven responses** – Directs users to helpful pages
* 📂 **Fully customizable** – Easily extend the `intents.json` file

---

## 🗂 Project Structure

```
├── intents.json          # Contains all intents, patterns, and responses
├── bot.py                # Main chatbot engine
├── README.md             # Documentation and setup guide
```

---

## 📦 Requirements

Ensure you have Python 3.x installed. Then install the following:

```bash
pip install nltk
python -m nltk.downloader punkt wordnet omw-1.4
```

---

## ⚙️ How It Works

### Step 1: Intent Matching

* User input is preprocessed (lowercased, tokenized, lemmatized).
* Each word is compared against a synonym map.
* If a match is found, a response or URL is immediately returned.

### Step 2: Pattern Scoring (Fallback)

* If no keyword match is found, the bot scores each predefined pattern by counting how many of its words appear in the user input.
* The intent with the highest score wins.

### Step 3: Default Fallback

* If nothing matches, a polite fallback message is shown.

---

## 🧪 Example

```bash
Chatbot: Hello! Ask me anything (type 'exit' to quit).
You: What is the admission procedure?
Chatbot: For information on application process, please visit https://example.com/application-process

You: What are your hours?
Chatbot: Our office is open from 9 AM to 5 PM, Monday through Friday.
```

---

## ✍️ Customizing Intents

All intents and their patterns/responses live in `intents.json`. Each entry looks like this:

```json
{
  "tag": "tuition_fees",
  "patterns": ["tuition fees", "fee structure", "how much is tuition"],
  "responses": ["For information on tuition fees, please visit https://example.com/tuition-fees"]
}
```

To add more:

* Add a new object under `intents`
* Provide several pattern examples (questions users might ask)
* Include one or more responses (URLs, text, etc.)

---

## 📈 Scalability Tips

* Add **more synonyms** in the `synonyms_map` dictionary inside `bot.py`
* Expand the `intents.json` with broader, deeper categories (housing, transport, health, etc.)
* Add **fuzzy matching** (e.g., via `rapidfuzz`) for typo tolerance
* Use logging to track unknown questions for future improvements

---

## 🤝 Contributions

Feel free to fork, extend, or suggest improvements! This is a lightweight foundation for anyone looking to build a FAQ bot for a university, company, or institution.

---

## 📄 License

This project is released under the MIT License. See `LICENSE` for details.

---

## 🧠 Inspired By

* [Real Python’s Chatbot Guide](https://realpython.com/python-chat-bot/)
* [Rasa Rule-Based Dialogue](https://rasa.com/docs/rasa/rule-based-dialogue/)
* [Tech with Tim – Chatbot Video](https://www.youtube.com/watch?v=8ext9G7xspg)
* [W3Schools Python Regex](https://www.w3schools.com/python/python_regex.asp)

---

Built with 💬 by aspiring conversational AI developers.
