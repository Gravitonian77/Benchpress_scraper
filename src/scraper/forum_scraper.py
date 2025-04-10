import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_bodybuilding_forum(search_term, max_pages=3):
    base_url = "https://forum.bodybuilding.com"
    search_url = f"{base_url}/search.php?do=process"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    posts = []

    for page in range(1, max_pages + 1):
        payload = {
            'query': search_term,
            'titleonly': 1,
            'searchthreadid': 0,
            'exactname': 1,
            'starteronly': 0,
            'forumchoice[]': ['9'],  # Example: Workout Programs subforum
            'do': 'process',
            'page': page
        }

        try:
            response = requests.post(search_url, data=payload, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find_all("a", class_="title")

            for link in results:
                title = link.get_text(strip=True)
                href = link.get('href')
                full_url = base_url + href if href else ''
                posts.append({"title": title, "url": full_url})

        except Exception as e:
            print(f"[Page {page}] Failed: {e}")
            continue

    return pd.DataFrame(posts)

def save_forum_data(df, filename="forum_results.csv"):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    output_dir = os.path.join(project_root, "data/raw")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} posts to {output_path}")



if __name__ == "__main__":
    search_term = "bench press plateau"
    df = scrape_bodybuilding_forum(search_term)
    save_forum_data(df)
