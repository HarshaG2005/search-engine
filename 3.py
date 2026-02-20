from nltk.stem import PorterStemmer
import math
import exercises.ex1 as ex
ps = PorterStemmer()
recipes = [
    {"id": 1, "title": "Coconut Curry", "text": "coconut milk curry powder"},
    {"id": 2, "title": "Prawn Curry", "text": "prawn in coconut curry isso"},
    {"id": 3, "title": "Dhal Curry", "text": "a lentil curry coconut"},
    {"id": 4, "title": "Isso Curry", "text": "isso prawn spicy curry"},
    {"id": 5, "title": "Fish Ambul Thiyal", "text": "fish sour spicy in goraka"},
]
indexes=ex.makeIndex(recipes)
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
print(f'this->{score("coconut",recipes[0],indexes,recipes)}')