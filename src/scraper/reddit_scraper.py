import configparser
import praw
import os
import pandas as pd

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../../config.ini'))

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
output_path = os.path.join(project_root, "data/raw/reddit_data.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

reddit = praw.Reddit(   client_id=config['reddit']['client_id'],
                        client_secret=config['reddit']['client_secret'],
                        user_agent=config['reddit']['user_agent']   )

def scrape_reddit(query, subreddit_list,limit=100):
    results = []
    subreddit = reddit.subreddit('+'.join(subreddit_list))
    for post in subreddit.search(query, limit=limit):
        post.comments.replace_more(limit=0)
        top_comments = [comment.body for comment in post.comments[:5]]
        results.append({
            'title': post.title,
            'content': post.selftext,
            'comments':  " || ".join(top_comments),
            'score': post.score,
            'created': post.created_utc,
            'subreddit': post.subreddit.display_name
        })
        print("Title:", post.title)

    return pd.DataFrame(results)

if __name__ == '__main__':
    df = scrape_reddit('bench press plateau', ['fitness', 'powerlifting', 'bodybuilding'])
    df.to_csv(output_path, index=False)
    print(type(df))
    print(df.shape)
    print(f"Saved {len(df)} posts to {output_path}")


