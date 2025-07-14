# 🧠 Stock Market Sentiment Analyzer using Financial News (XGBoost + NLP)

## 🔍 Description

This project builds an end-to-end sentiment classification system that reads real-world financial news headlines and classifies them into **positive**, **neutral**, or **negative** sentiments using Natural Language Processing (NLP) and XGBoost.

It is based on the **Financial PhraseBank dataset**, a curated collection of finance-specific headlines, and demonstrates how sentiment analysis can be automated for applications like:

* Stock market trend analysis
* Market monitoring dashboards
* Automated trading bots

---

## 💡 What this Project Does

* Cleans and preprocesses financial news text
* Converts raw text to TF-IDF vectors
* Trains an **XGBoost** classifier on the labeled dataset
* Evaluates model using precision, recall, f1-score
* Visualizes data using **Word Clouds** for each sentiment
* Deploys a **Streamlit-based web app** for real-time sentiment prediction

---

## 📦 Tech Stack

* **Python** (Pandas, Numpy)
* **Scikit-learn** (TF-IDF Vectorizer, evaluation metrics)
* **XGBoost** for model training
* **Matplotlib** and **WordCloud** for visualization
* **Streamlit** for interactive frontend

---

## 🚀 Live Demo

> 🔗 \https://stock-market-sentiment-analyze-fwrvwheqnkbrnqxfy2i5lp.streamlit.app/

---

## 🗂️ Folder Structure

```
📆 sentiment-analyzer/
 ├── app.py
 ├── sentiment_model.pkl
 ├── tfidf_vectorizer.pkl
 ├── requirements.txt
 ├── README.md
 └── financial-news.csv
```

---

## 👨‍💻 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## 📊 Model Performance (XGBoost)

* **Accuracy**: \~74%
* Handles **imbalanced sentiment classes** effectively
* Optimized for **real-world financial headlines**

---

## 🎓 Dataset Reference

* [Financial PhraseBank - Sentences with Annotated Sentiment](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis)

---

## 🙏 Acknowledgements

Thanks to the creators of the Financial PhraseBank and open-source communities for tools that made this possible!

---
