from textblob import TextBlob

def analyze(text):
    tb = TextBlob(text)
    d = dict()
    d['sentiment'] = 'positive' if tb.sentiment.polarity > 0 else 'negative'
    d['polarity'] = tb.sentiment.polarity
    d['subjectivity'] = tb.sentiment.subjectivity
    return d

