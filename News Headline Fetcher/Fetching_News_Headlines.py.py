#This Python script fetches headlines from multiple news sources' RSS feeds and displays them in the console. 
import requests
import feedparser

# Define a list of news sources (RSS feed URLs)
news_sources = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",  # New York Times
    "https://feeds.bbci.co.uk/news/rss.xml",  # BBC News
    "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera
    # Add more news sources here
]

def fetch_news_headlines():
    headlines = []
    
    for source in news_sources:
        try:
            # Parse the RSS feed
            feed = feedparser.parse(source)

            # Extract and append headlines
            for entry in feed.entries:
                headline = {
                    "source": feed.feed.title,
                    "title": entry.title,
                    "link": entry.link,
                }
                headlines.append(headline)

        except Exception as e:
            print(f"Error fetching news from {source}: {e}")

    return headlines

def display_headlines(headlines):
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. [{headline['source']}] {headline['title']}")
        print(f"   Link: {headline['link']}\n")

if __name__ == "__main__":
    print("Fetching news headlines...\n")
    news_headlines = fetch_news_headlines()
    display_headlines(news_headlines)
