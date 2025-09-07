import tweepy
from sentiment_analysis import get_sentiment_score
from alerts import send_alert
from config import TWITTER_BEARER_TOKEN, INFLUENCER_USER_IDS, ALERT_THRESHOLD

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.author_id in INFLUENCER_USER_IDS:
            score = get_sentiment_score(tweet.text)
            print(f"Influencer Tweet: {tweet.text} | Sentiment: {score}")
            if abs(score) >= ALERT_THRESHOLD:
                send_alert(tweet.text, score)

def start_stream():
    stream = MyStream(bearer_token=TWITTER_BEARER_TOKEN)
    stream.add_rules(tweepy.StreamRule("from:" + " OR from:".join(INFLUENCER_USER_IDS)))
    stream.filter(tweet_fields=["author_id", "created_at", "text"])

if __name__ == "__main__":
    start_stream()
