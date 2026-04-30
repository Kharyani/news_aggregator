from fetchers.newsapi import get_news
import json

def display_news(news):
    """Print formatted news output"""
    if not news:
        print("No news found.")
        return

    for article in news[:5]:  # limit articles
        print("\n" + "=" * 60)
        print(f"📰 {article.get('title', 'No Title')}")
        print(f"📌 Source: {article['source'].get('name', 'Unknown')}")
        print(f"🔗 {article.get('url', 'No URL')}")
        print("=" * 60)

def save_news(news, filename="news.json"):
    """Save news to JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(news, f, indent=4, ensure_ascii=False)
    print(f"\n💾 News saved to {filename}")

def main():
    while True:
        print("\n" + "=" * 30)
        print("      📰 NEWS AGGREGATOR")
        print("=" * 30)
        print("1. Tech News")
        print("2. Sports News")
        print("3. Business News")
        print("4. General News")
        print("5. Exit")
        print("=" * 30)

        choice = input("Enter your choice: ")

        if choice == "1":
            news = get_news("technology")

        elif choice == "2":
            news = get_news("sports")

        elif choice == "3":
            news = get_news("business")

        elif choice == "4":
            news = get_news("general")

        elif choice == "5":
            print("👋 Exiting News Aggregator...")
            break

        else:
            print("❌ Invalid choice, try again.")
            continue

        # Display and save
        display_news(news)
        save_news(news)

if __name__ == "__main__":
    main()