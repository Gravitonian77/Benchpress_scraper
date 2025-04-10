import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter

#nltk.download('punkt')
#nltk.download('stopwords')
nltk.data.path.append('/home/raven/nltk_data')

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
    return tokens

def analyze_issues(df):
    df['content'] = df['content'].fillna('').astype(str)
    df['comments'] = df['comments'].fillna('').astype(str)
    all_text = " ".join(df['content'] + " " + df['comments'])
    tokens = preprocess_text(all_text)
    common_issues = Counter(tokens).most_common(20)
    return common_issues

if __name__ == '__main__':
    df = pd.read_csv('../../data/raw/reddit_data.csv')
    issues = analyze_issues(df)
    print(issues)