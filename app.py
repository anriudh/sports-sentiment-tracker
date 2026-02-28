import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sports Sentiment Tracker", layout = "wide")
st.title("Sports Sentiment Tracker")
st.markdown("Sentiment analysis of the latest football/soccer news using VADER NLP")

df = pd.read_csv("data/articles_with_sentiment.csv")
df["published_at"] = pd.to_datetime(df["published_at"])

total = len(df)
positive = len(df[df["sentiment_label"] == "Positive"])
negative = len(df[df["sentiment_label"] == "Negative"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Articles", total)
col2.metric("Positive", f"{positive} ({round(positive/total*100)}%)")
col3.metric("Negative", f"{negative} ({round(negative/total*100)}%)")

st.subheader("Sentiment Overview")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    sns.countplot(data=df, x="sentiment_label", hue="sentiment_label",
                  palette={"Positive": "green", "Neutral": "gray", "Negative": "red"},
                  order=["Positive", "Neutral", "Negative"], legend=False, ax=ax1)
    ax1.set_title("Sentiment Distribution")
    ax1.set_xlabel("Sentiment")
    ax1.set_ylabel("Articles")
    st.pyplot(fig1)

with col2:
    df["date"] = df["published_at"].dt.date
    daily = df.groupby("date")["compound"].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    sns.lineplot(data=daily, x="date", y="compound", ax=ax2)
    ax2.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    ax2.set_title("Avg Sentiment Over Time")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Avg Compound Score")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(8, 3))
sns.histplot(df["compound"], bins=20, kde=True, color="steelblue", ax=ax3)
ax3.axvline(0, color="red", linestyle="--", linewidth=0.8)
ax3.set_title("Distribution of Sentiment Scores")
ax3.set_xlabel("Compound Score")
ax3.set_ylabel("Articles")
st.pyplot(fig3)

st.subheader("Article-Level Sentiment")

filter_option = st.selectbox("Filter by Sentiment", ["All", "Positive", "Neutral", "Negative"])

if filter_option == "All":
    filtered_df = df
else:
    filtered_df = df[df["sentiment_label"] == filter_option]

st.dataframe(
    filtered_df[["published_at", "source", "title", "compound", "sentiment_label"]].sort_values("published_at", ascending=False),
    use_container_width=True
)
