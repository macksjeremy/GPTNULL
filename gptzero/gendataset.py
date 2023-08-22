import pandas as pd
import re
from textattack.datasets import Dataset

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def contains_alpha(input):
    search_results = re.search('[a-zA-Z]', input)
    if search_results == None:
        return False
    else:
        return True
    return search_results

def isurl(input):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, input) is not None


def printline():
    print("------------------------------------------")


def gen_data():
    limit = 150000 - 1
    df = pd.read_csv("GPT-wiki-intro.csv")
    df = df.iloc[:limit]
    formatted_data = []
    true = list(df["generated_intro"])
    false = list(df["wiki_intro"])
    for i in range(len(true)):
        formatted_data.append((true[i],0))
        formatted_data.append((false[i],1))
    return formatted_data

data = gen_data()
dataset = Dataset(data)
data = Dataset
