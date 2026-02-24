import math
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.indexer import indexes, recipes
from nltk.stem import PorterStemmer

ps = PorterStemmer()


def stem(word):
    word=word.lower()
    return ps.stem(word)


def idf(query,indexes,recipes):
    docs_containing_query=indexes.get(query,[])
    if len(docs_containing_query) == 0:
        return 0
    return math.log(len(recipes)/len(docs_containing_query))


def tf(query,recipe,indexes):
    content=recipe['text']+" "+recipe['title']
    content=content.lower().split()
    words=[ps.stem(word)for word in content]
    count=words.count(query)
    return count/len(words)


def score(query,recipe,indexes,recipes):
    query=stem(query)
    return tf(query,recipe,indexes)*idf(query,indexes,recipes)



def search(query, recipes, indexes):
    results = []
    for recipe in recipes:
        s = score(query, recipe, indexes, recipes)
        if s > 0:
            results.append((recipe, s))
    results.sort(key=lambda x: x[1], reverse=True)
    return results



if __name__ == "__main__":
    results = search("curry", recipes, indexes)
    for recipe, score in results:
        print(f"{recipe['title']} -> {score}")