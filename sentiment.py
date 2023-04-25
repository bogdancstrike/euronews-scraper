from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def analyze_sentiment(sentiment):
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def generate_sentiment(text):
    sentiment = get_sentiment(text)
    sentiment_label = analyze_sentiment(sentiment)
    return sentiment_label