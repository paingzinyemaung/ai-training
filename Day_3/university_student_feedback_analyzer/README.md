# AI-Powered University Student Feedback Analyzer

A Python NLP project that analyzes university student feedback. It preprocesses text, demonstrates Bag of Words and TF-IDF, generates sentence embeddings, trains sentiment and category classifiers, and provides a Gradio interface.

## Dataset

`student_feedback.csv` contains 72 feedback messages and the required columns:

- `feedback_id`: unique feedback identifier
- `feedback_text`: original student feedback
- `sentiment`: Positive, Negative, or Neutral
- `category`: Teaching, Laboratory, Facilities, or Administration

The original feedback text is kept unchanged. Preprocessing is performed on a separate working copy.

## Requirements

- Python 3.10 or newer
- Internet connection for the first download of the pretrained Sentence Transformer model

## Setup

Open a terminal in this project folder and run:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The program prints preprocessing examples, sample BoW and TF-IDF features, embedding information, cosine similarity, and classification evaluation results. Gradio then provides a local URL in the terminal. Open that URL in a browser to use the analyzer.

## Assignment tasks covered

1. **Dataset preparation:** CSV dataset with more than 30 feedback messages.
2. **Text preprocessing:** lowercasing, punctuation normalization, whitespace normalization, tokenization, and stop-word removal.
3. **Text representation:** CountVectorizer (Bag of Words) and TfidfVectorizer (TF-IDF).
4. **Text embeddings:** `sentence-transformers/all-MiniLM-L6-v2` creates embeddings for five feedback messages; cosine similarity is calculated for two selected messages.
5. **Classification:** train/test split, TF-IDF, and Multinomial Naive Bayes for sentiment prediction. A separate classifier predicts the feedback category.
6. **Interface:** Gradio accepts feedback and displays predicted sentiment, predicted category, and processed text summary.

## Notes

- This is a small educational dataset created for the assignment. Model scores are only a demonstration and should not be treated as reliable measurements of real university-wide feedback.
- The first run may take longer because the pretrained embedding model needs to be downloaded.
