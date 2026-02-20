from nltk.stem import PorterStemmer
import math

ps = PorterStemmer()
recipes = [
    {"id": 1, "title": "Coconut Curry", "text": "coconut milk curry powder"},
    {"id": 2, "title": "Prawn Curry", "text": "prawn in coconut curry isso"},
    {"id": 3, "title": "Dhal Curry", "text": "a lentil curry coconut"},
    {"id": 4, "title": "Isso Curry", "text": "isso prawn spicy curry"},
    {"id": 5, "title": "Fish Ambul Thiyal", "text": "fish sour spicy in goraka"},
]
def makeIndex(recipes):
    index={}
    stopwords = {"and", "the", "with", "a", "of", "in", "is"}
    for recipe in recipes:
        content=recipe['text']+" "+recipe['title']#to include the title in the search   
        words=content.split()
        for word in words:
            word=word.lower()#to make the search case insensitive
            word=ps.stem(word)
            if word in stopwords:
                continue
            if word not in index:  
                index[word]=[]
            if recipe['id'] not in index[word]:
                index[word].append(recipe['id'])
    return index
indexes=makeIndex(recipes)



def search_word(word,indexes):
    word=word.lower()#to make the search case insensitive
    word=ps.stem(word)
    return indexes.get(word,[])
 
def search_2_words(word1,word2,indexes):
    word1=word1.lower()#to make the search case insensitive
    word2=word2.lower()#to make the search case insensitive
    word1=ps.stem(word1)
    word2=ps.stem(word2)
    ids1=set(indexes.get(word1,[]))#set(None) doesn't give an empty set — it crashes with a TypeError. set([]) gives an empty set. Small but important distinction to have right in your mental model.
    ids2=set(indexes.get(word2,[]))
    if ids1 and ids2 :
        return list(ids1 & ids2)#lists dont have intersection but sets do
    elif ids1:
        return list(ids1)
    elif ids2:
        return list(ids2)
    else:
        return None
# print(search_word("spicy", indexes))        # should return [4, 5]
# print(search_2_words("prawns", "spici", indexes))  # should return [4]
# print(search_2_words("coconuts", "curry", indexes)) # what do you expect here?

def idf(word, index, total_recipes):
    docs_containing_word = len(index.get(word, []))
    if docs_containing_word == 0:
        return 0
    return math.log(total_recipes / docs_containing_word)
if __name__ == "__main__":
    print(f'this idf of "coconut": {idf("coconut", indexes, len(recipes))}')  # low because it appears in many recipes
    print(f'this idf of "isso": {idf("isso", indexes, len(recipes))}')   # higher because it appears in fewer recipes   
    print(f'this idf of "goraka": {idf("goraka", indexes, len(recipes))}'  ) # highest because it appears in only one recipe
    print(indexes)