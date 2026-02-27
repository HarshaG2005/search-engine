import string

from nltk import PorterStemmer
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))

ps = PorterStemmer()


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    stemmed_words = [ps.stem(word) for word in words if word not in stopwords]
    return stemmed_words
