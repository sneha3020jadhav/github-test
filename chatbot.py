import nltk
import streamlit as st
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('vader_lexicon')

def get_sentiment(text):
    # Analyze sentiment using TextBlob (general sentiment)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Analyze sentiment using VADER (specific emotions)
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    compound_score = scores['compound']

    if polarity > 0:
        return "Positive", compound_score
    elif polarity < 0:
        return "Negative", compound_score
    else:
        return "Neutral", compound_score

def get_response(user_input):
    sentiment, score = get_sentiment(user_input)
    if sentiment == "Positive":
        return "I'm glad you're feeling positive! 😊 What's making you happy?"
    elif sentiment == "Negative":
        return "I'm sorry to hear that you're feeling down. 😔 Is there anything I can do to help?"
    else:
        return "I see. 🤔 Tell me more about what's on your mind."

# Streamlit app layout
st.title("Simple Chatbot")
st.write("Hi! I'm a simple chatbot. How are you feeling today?")

# User input
user_input = st.text_input("You: ", "")

# Chatbot response
if user_input:
    response = get_response(user_input)
    st.write(f"Bot: {response}")

# Option to end the chat
if st.button("End Chat"):
    st.write("Goodbye! Take care. 👋")
    st.stop()
