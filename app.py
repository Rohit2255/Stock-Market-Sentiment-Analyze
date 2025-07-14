# app.py

import streamlit as st
import pickle
import numpy as np

# Load vectorizer and model
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
model = pickle.load(open("sentiment_model.pkl", "rb"))

# Title
st.set_page_config(page_title="Stock Market Sentiment Analyzer")
st.title("📊 Stock Market Sentiment Analyzer")
st.markdown("Enter any financial news headline or sentence below, and we'll predict its sentiment!")

# User Input
user_input = st.text_area("📰 Enter a financial sentence:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence to analyze.")
    else:
        # Preprocess + Vectorize
        transformed_input = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(transformed_input)[0]

        sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        st.success(f"🧠 Predicted Sentiment: **{sentiment_map[prediction]}**")
