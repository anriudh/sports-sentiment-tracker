# 📊 Sports Sentiment Tracker

A small end-to-end data pipeline that collects recent football news, analyzes sentiment using NLP, and visualizes the results in an interactive dashboard.

I built this project to practice working with **real APIs, modular pipelines, and NLP on real-world text**, rather than curated datasets.

**Live Demo:**
https://sports-sentiment-tracker.streamlit.app/

---

## 🚀 What it does

The workflow runs in three stages:

1. **Fetch news** — pulls up to 100 recent football articles using NewsAPI
2. **Analyze sentiment** — scores headlines/descriptions using VADER
3. **Visualize results** — displays trends and distributions via Streamlit

Each article receives:

* A compound sentiment score (-1 to +1)
* A label: Positive, Neutral, or Negative

---

## 🧠 Key Design Decisions

* **Used VADER sentiment analysis** because I had previously studied it in college and wanted hands-on experience applying it to real data.
* Chose a **modular pipeline structure** to simulate a simple ETL workflow.
* Focused on **headlines + descriptions** since full article text isn’t available in the free NewsAPI tier.

---

## ⚙️ Tech Stack

* Data Fetching — NewsAPI, requests
* NLP — VADER Sentiment
* Processing — pandas
* Visualization — matplotlib, seaborn
* Dashboard — Streamlit

---

## 🏗️ Project Structure

```
src/
 ├── scraper.py        # Fetch articles
 ├── sentiment.py      # Score sentiment
 └── visualizer.py     # Generate charts
app.py                 # Streamlit dashboard
```

---

## ▶️ Running Locally

```bash
git clone https://github.com/anriudh/sports-sentiment-tracker.git
cd sports-sentiment-tracker
pip install -r requirements.txt
```

Create a `.env` file:

```
NEWS_API_KEY=your_key_here
```

Run pipeline:

```bash
python src/scraper.py
python src/sentiment.py
streamlit run app.py
```

---

## 📈 Dashboard Highlights

The dashboard allows quick exploration of:

* Overall sentiment distribution
* Trend of sentiment over time
* Score histogram
* Filterable article table

---

## ⚠️ Limitations

* NewsAPI free tier restricts article count and provides only partial text.
* Headlines often use neutral language, making sentiment classification challenging.
* VADER is rule-based and may miss sarcasm or deeper context.

---

## 🎯 Why this project matters

This project helped me move beyond notebook-only ML work and practice building a **complete data workflow** — from data ingestion to analysis to visualization.

It also provided hands-on experience dealing with **real, messy text data**, which behaves very differently from clean academic datasets.

---

## 🔮 Possible Improvements

* Add in-dashboard data refresh
* Compare VADER with transformer-based models
* Track sentiment for specific teams or leagues
