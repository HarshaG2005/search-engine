from nltk import PorterStemmer

ps=PorterStemmer()
def preprocess(text):
    stopwords = {"and", "the", "with", "a", "of", "in", "is"}
    text=text.lower()
    words=text.split()
    stemmed_words=[ps.stem(word) for word in words if word not in stopwords]
    return stemmed_words