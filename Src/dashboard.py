import streamlit as st
from data_processing import load_and_process_data
from sentiment_analysis import add_sentiment_column
from config import HISTORICAL_TWEETS_PATH, BITCOIN_PRICE_PATH
import plotly.express as px

st.title("Bitcoin Sentiment Dashboard")

df = load_and_process_data(HISTORICAL_TWEETS_PATH, BITCOIN_PRICE_PATH)
df = add_sentiment_column(df)

st.subheader("Historical Sentiment vs BTC Price")
fig = px.scatter(df, x="sentiment", y="price_usd", color="user_type", hover_data=["tweet_text"])
st.plotly_chart(fig)

st.subheader("Latest Tweets")
st.dataframe(df[['created_at','user_type','tweet_text','sentiment']].sort_values(by='created_at', ascending=False))
