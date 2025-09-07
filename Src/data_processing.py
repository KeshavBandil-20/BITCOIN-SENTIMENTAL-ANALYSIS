import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

stop_words = set(stopwords.words('english'))

def clean_tweet(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    filtered = [w for w in tokens if w not in stop_words]
    return ' '.join(filtered)

def load_and_process_data(tweet_path, price_path):
    tweets = pd.read_csv(tweet_path)
    prices = pd.read_csv(price_path)
    tweets['clean_text'] = tweets['tweet_text'].apply(clean_tweet)
    merged = pd.merge(tweets, prices, left_on='created_at', right_on='timestamp', how='left')
    return merged
