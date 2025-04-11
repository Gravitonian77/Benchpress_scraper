import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    custom_junk = {
        'like', 'get', 'would', 'one', 'really', 'try', 'go', 'even',
        'also', 'lot', 'something', 'could', 'maybe', 'think', 'still',
        'just', 'know', 'thing', 'sure', 'make', 'use', 'way', 'many',
        'going', 'well', 'see', 'done', 'got', 'etc', 'yes', 'thanks'
    }
    stop_words.update(custom_junk)
    return [word for word in tokens if word.isalpha() and word not in stop_words]

def load_and_process_text(csv_path):
    df = pd.read_csv(csv_path)
    df['content'] = df['content'].fillna('').astype(str)
    df['comments'] = df['comments'].fillna('').astype(str)
    all_text = " ".join(df['content'] + " " + df['comments'])
    return Counter(preprocess_text(all_text)).most_common(20)

def plot_issues(freq_data, output_path):
    words, counts = zip(*freq_data)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=list(counts), y=list(words))
    plt.xlabel("Mentions")
    plt.ylabel("Issue Keyword")
    plt.title("Most Common Bench Press Issues")
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"Saved plot to {output_path}")

if __name__ == "__main__":
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    input_path = os.path.join(base_dir, "data/raw/reddit_data.csv")
    output_path = os.path.join(base_dir, "data/processed/issues_plot.png")

    freq_data = load_and_process_text(input_path)
    plot_issues(freq_data, output_path)
