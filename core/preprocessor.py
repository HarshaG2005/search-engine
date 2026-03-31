import string
import nltk 
from nltk import PorterStemmer
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))
sl_stopwords={"sri","lankan","srilankan","srilanka","lanka"}

ps = PorterStemmer()


def preprocess(text):
    """Lowercase, remove punctuation, tokenize, remove stopwords, and stem."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    stemmed_words = [ps.stem(word) for word in words if word not in stopwords]
    final_words=[word for word in stemmed_words if word not in sl_stopwords]
    return final_words
