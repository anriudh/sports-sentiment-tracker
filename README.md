# Sports Sentiment Tracker

A data pipeline that fetches live football/soccer news via the NewsAPI, runs VADER sentiment analysis on article headlines and descriptions, and presents the results through an interactive Streamlit dashboard.

**Live demo:** https://sports-sentiment-tracker-iwrofipykrgk3osjrxszdt.streamlit.app/

---

## What it does

- Fetches up to 100 recent football/soccer news articles using the NewsAPI
- Scores each article's sentiment using VADER NLP (compound score from -1 to +1)
- Classifies articles as Positive, Neutral, or Negative
- Visualizes sentiment distribution, trends over time, and score spread
- Displays an interactive, filterable article table with scores

---

## Tech Stack

| Area | Tools |
|------|-------|
| Data Fetching | `requests`, NewsAPI |
| NLP / Sentiment | `vaderSentiment` |
| Data Handling | `pandas` |
| Visualization | `matplotlib`, `seaborn` |
| Dashboard | `streamlit` |
| Environment | `python-dotenv` |

---

## Project Structure

```
sports-sentiment-tracker/
├── src/
│   ├── scraper.py        # Fetches articles from NewsAPI, saves to CSV
│   ├── sentiment.py      # Runs VADER sentiment analysis, outputs scored CSV
│   └── visualizer.py     # Generates and saves chart images
├── data/                 # CSVs and chart outputs (gitignored raw data)
├── app.py                # Streamlit dashboard
├── requirements.txt
└── runtime.txt
```

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/anriudh/sports-sentiment-tracker.git
cd sports-sentiment-tracker
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API key**

Create a `.env` file in the project root:
```
NEWS_API_KEY=your_newsapi_key_here
```
Get a free key at [newsapi.org](https://newsapi.org).

**4. Run the pipeline**
```bash
python src/scraper.py       # Fetch articles
python src/sentiment.py     # Score sentiment
```

**5. Launch the dashboard**
```bash
streamlit run app.py
```

---

## Dashboard Features

- **Summary metrics** -- total articles, % positive, % negative
- **Sentiment distribution** -- bar chart of Positive / Neutral / Negative counts
- **Sentiment over time** -- daily average compound score trend line
- **Score histogram** -- distribution of all compound scores
- **Filterable article table** -- browse and filter articles by sentiment label

## Roadmap
- [ ] In-app data refresh button to fetch latest articles without running scripts manually