from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

def add_sentiment_column(df):
    df['sentiment'] = df['clean_text'].apply(get_sentiment_score)
    return df
