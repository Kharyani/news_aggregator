News Aggregator (Python CLI Project)
📌 Overview

The News Aggregator is a Python-based command-line application that fetches real-time news from the NewsAPI and displays it in a clean, structured format. It allows users to browse news by category, view top headlines, and save results locally for later use.

This project demonstrates API integration, modular programming, and CLI-based UI design in Python.

🚀 Features
🔎 Fetch real-time news using NewsAPI
🗂️ Category-based filtering:
Technology
Sports
Business
General
🖥️ Interactive CLI menu system
📰 Clean and formatted news display
📄 Limit results to top 5 articles
💾 Save news data to JSON file
🧩 Modular code structure (fetchers + main logic)
🛠️ Tech Stack
Python 3.x
Requests library
NewsAPI (https://newsapi.org
)
📁 Project Structure
news_aggregator/
│── main.py                # Main CLI application
│── config.py              # API key and URL configuration
│── news.json              # Auto-generated saved news file
│── fetchers/
│     └── newsapi.py      # API handling logic
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/news-aggregator.git
cd news-aggregator
2. Install dependencies
pip install requests
3. Add your API key

Open config.py and add:

NEWS_API_KEY = "your_api_key_here"
NEWSAPI_URL = "https://newsapi.org/v2/top-headlines"
▶️ How to Run

Run the application using:

python main.py
🧭 Menu Options
1. Tech News
2. Sports News
3. Business News
4. General News
5. Exit

Select a number and press Enter to fetch live news.

📸 Sample Output
📰 NEWS 1
Title: AI revolution in technology sector
📌 Source: BBC News
🔗 https://example.com

📰 NEWS 2
Title: Global sports update
📌 Source: ESPN
🔗 https://example.com
💾 Output Storage

All fetched news is automatically saved in:

news.json
📚 Learning Outcomes

This project helps you understand:

API integration in Python
JSON data handling
CLI application design
Modular programming structure
Real-world project architecture
🔮 Future Improvements
🌐 Web dashboard (Flask / Streamlit)
🔍 Search news by keyword
❤️ Bookmark favorite articles
🧠 AI-based news summarization
📊 Analytics dashboard for trending news
👨‍💻 Author

Developed as a learning project for mastering Python API integration and real-time data handling.
