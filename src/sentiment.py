from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()

    df["compound"] = df.apply(
        lambda row: analyzer.polarity_scores(
            str(row["title"]) + " " + str(row["description"])
        )["compound"],
        axis=1
    )

    df["sentiment_label"] = df["compound"].apply(
        lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
    )

    df.to_csv("data/articles_with_sentiment.csv", index=False)
    print(df[["title", "compound", "sentiment_label"]].head(10))
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw_articles.csv")
    analyze_sentiment(df)