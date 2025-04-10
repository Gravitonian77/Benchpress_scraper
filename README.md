# Bench Press Plateau Analyzer

### 🚧 This project is a work in progress. Core functionality is being built and refined.

A Python-based web scraper and analyzer designed to uncover common problems that people face while striving to achieve a 225 lb bench press. The scraper gathers user experiences from popular fitness communities online and analyzes the data to provide meaningful insights into common issues.

---

## 📌 Project Overview

The goal of this project is to:

- Identify and scrape relevant discussions on bench press plateaus from popular fitness forums, especially Reddit.
- Extract and analyze textual data to discover the most frequent challenges encountered by weightlifters.
- Provide visualizations and insights based on data-driven analysis.

---

## 🔧 Project Structure

```
benchpress-scraper/
├── data/
│   ├── raw/              # Raw scraped data (CSV)
│   └── processed/        # Processed data and visualizations
├── notebooks/            # Jupyter notebooks for data exploration
├── src/
│   ├── scraper/
│   │   └── reddit_scraper.py   # Reddit scraping logic
│   ├── analysis/
│   │   ├── analyzer.py         # Text analysis logic
│   │   └── visualize.py        # Visualization logic
│   └── utils/
│       └── helpers.py          # Common helper functions
├── .gitignore
├── config.ini             # API credentials (hidden)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (`venv`)

### Installation

Create and activate your virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

Configure your API credentials:

- Create a Reddit API application [here](https://www.reddit.com/prefs/apps).
- Place your credentials in `config.ini`:

```ini
[reddit]
client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
user_agent = script:benchpress.scraper:v1.0 (by u/YOUR_USERNAME)
```

---

## 🖥️ Usage

### Scraping data

Scrape posts related to bench press plateaus:

```bash
python src/scraper/reddit_scraper.py
```

### Analyzing data

Analyze common issues:

```bash
python src/analysis/analyzer.py
```

### Visualization

Visualize common issues:

```bash
python src/analysis/visualize.py
```

Visualizations will be saved to:

```
data/processed/issues_plot.png
```

---

## 📈 Example Output

- **Top Issues Identified:**
  - Shoulders
  - Triceps
  - Plateau
  - Technique

---

## ⚙️ Technologies Used

- **PRAW**: Reddit API wrapper
- **Pandas**: Data manipulation
- **NLTK**: Text processing
- **Matplotlib & Seaborn**: Data visualization

---

## 📖 Future Development

- Expand scraping to additional fitness forums and social media.
- Incorporate advanced NLP techniques like sentiment analysis and topic modeling.
- Create a user-friendly dashboard for interactive analysis.

---

## 🙌 Contributing

Feel free to contribute by opening issues, submitting feature requests, or sending pull requests. All contributions are welcome!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
