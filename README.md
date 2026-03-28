# Sports Sentiment Tracker

A small end-to-end data pipeline that collects recent football news, analyzes sentiment using NLP, and visualizes the results in an interactive dashboard.

I built this to practice working with real APIs, modular pipelines, and NLP on real-world text, rather than curated datasets.

**Live demo:** https://sports-sentiment-tracker.streamlit.app/

---

## What it does

The workflow runs in three stages:

1. **Fetch news** — pulls up to 100 recent football articles using NewsAPI
2. **Analyze sentiment** — scores headlines and descriptions using VADER
3. **Visualize results** — displays trends and distributions via Streamlit

Each article gets a compound sentiment score (-1 to +1) and a label: Positive, Neutral, or Negative.

---

## Decisions I made

- Used VADER because I had studied it in college and wanted hands-on experience applying it to real data
- Went with a modular pipeline structure to simulate a simple ETL workflow
- Focused on headlines and descriptions since full article text isn't available on the free NewsAPI tier

---

## Tech Stack

| Area | Tools |
|------|-------|
| Data Fetching | NewsAPI, requests |
| NLP | vaderSentiment |
| Processing | pandas |
| Visualization | matplotlib, seaborn |
| Dashboard | Streamlit |

---

## Project Structure
```
data/
 ├── csv/         # stored datasets
 └── plots/       # generated charts
src/
 ├── scraper.py   # fetch articles
 ├── sentiment.py # score sentiment
 └── visualizer.py# generate charts
app.py            # Streamlit dashboard
```

---

## Running Locally
```bash
git clone https://github.com/anriudh/sports-sentiment-tracker.git
cd sports-sentiment-tracker
pip install -r requirements.txt
```

Create a `.env` file:
```
NEWS_API_KEY=your_key_here
```

Run the pipeline:
```bash
python src/scraper.py
python src/sentiment.py
streamlit run app.py
```

The dashboard also has a refresh button in the sidebar that re-fetches and re-analyzes articles without needing to run scripts manually.

---

## Dashboard

- Sentiment distribution across articles
- Average sentiment trend over time
- Score histogram
- Filterable article table by sentiment label
- Sidebar refresh button to pull latest articles on demand

---

## Limitations

- NewsAPI free tier limits article count and provides only partial text
- Headlines tend toward neutral language, which makes classification harder
- VADER is rule-based and doesn't catch sarcasm or context well

---

## What I learned

Moving beyond notebook-only work and building a complete data workflow — ingestion, analysis, visualization, deployment — was the main goal here. Dealing with real, messy text data also behaves very differently from clean academic datasets, which was a useful reality check.
