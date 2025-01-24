# Import necessary libraries
import requests
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# API Key for NewsAPI (get your free API key at https://newsapi.org/)
API_KEY = "b587f30ad5c34dcc9a1f9a2300ce5fdd"
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(keyword):
    """
    Fetches news articles based on a keyword using the NewsAPI.
    """
    params = {
        "q": keyword,
        "apiKey": API_KEY,
        "language": "en",
        "pageSize": 5  # Fetch top 5 articles
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        print("Error fetching news:", response.status_code)
        return []

def summarize_and_analyze(article):
    """
    Summarizes an article and performs sentiment analysis.
    """
    title = article["title"]
    description = article["description"] or "No description available."
    url = article["url"]
    
    # Perform sentiment analysis
    sentiment = sia.polarity_scores(description)
    sentiment_class = (
        "Positive" if sentiment["compound"] > 0.05
        else "Negative" if sentiment["compound"] < -0.05
        else "Neutral"
    )
    
    # Display results
    print("\nTitle:", title)
    print("Description:", description)
    print("Sentiment:", sentiment_class)
    print("Link to full article:", url)

def main():
    print("📰 Welcome to the News Summarizer and Sentiment Analyzer!")
    keyword = input("Enter a keyword to search for news (e.g., AI, technology): ")
    print("\nFetching news articles...\n")
    
    articles = fetch_news(keyword)
    if not articles:
        print("No articles found.")
        return
    
    print(f"Found {len(articles)} articles on '{keyword}':")
    for i, article in enumerate(articles, start=1):
        print(f"\nArticle {i}")
        summarize_and_analyze(article)

if __name__ == "__main__":
    main()