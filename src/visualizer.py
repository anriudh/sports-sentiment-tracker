import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/articles_with_sentiment.csv")
df["published_at"] = pd.to_datetime(df["published_at"])

#Chart 1: Sentiment Distribution (bar chart)
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="sentiment_label", hue="sentiment_label", palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}, order=["Positive", "Neutral", "Negative"], legend=False)
plt.title("Sentiment Distribution of Football News")
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.tight_layout()
plt.savefig("data/sentiment_distribution.png")
plt.show()

#Chart 2: Sentiment Over Time (line chart)
df["date"] = df["published_at"].dt.date
daily_sentiment = df.groupby("date")["compound"].mean().reset_index()

plt.figure(figsize=(10, 4))
sns.lineplot(data=daily_sentiment, x="date", y="compound")
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
plt.title("Average Sentiment Over Time - Football News")
plt.xlabel("Date")
plt.ylabel("Avg Compound Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/sentiment_over_time.png")
plt.show()

#Chart 3: Compound Score Histogram
plt.figure(figsize=(8, 4))
sns.histplot(df["compound"], bins=20, kde=True, color="steelblue")
plt.axvline(0, color="red", linestyle="--", linewidth=0.8)
plt.title("Distribution of Sentiment Scores - Football News")
plt.xlabel("Compound Score")
plt.ylabel("Number of Articles")
plt.tight_layout()
plt.savefig("data/sentiment_histogram.png")
plt.show()