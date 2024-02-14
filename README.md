## Sentiment Analysis API

A simple sentiment analysis example.

### Requirements
- Python versions 3.7, 3.8, 3.9, 3.10 or 3.11

### Usage

- Build

```
pip install -r requirements.txt 
```

- Run

```
python server.py
```

- Use

```
curl http://localhost:3000/sentiment -X POST -d '{"text":"The food was wonderful, not too spicy and not too mild; just perfect! I will come back for sure!"}' -H "Content-Type: application/json"
```

## Explanation
I'll explain what the output means in case you're not familiar with NLP and sentiment analysis.

The output of the sentiment analysis API contains three key pieces of information: polarity, sentiment, and subjectivity.
- Polarity: This is a probability score between -1 (negative) and 1 (positive). It indicates the overall sentiment leaning of the input text.
- Sentiment: this is a simple label like "positive," "negative," or "neutral" that directly corresponds to the polarity score above.
- Subjectivity: This a probability score between 0 (objective) and 1 (subjective). It indicates how much facts or personal opinions/feelings are expressed in the input text.
