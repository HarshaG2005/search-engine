recipes = [
    {"id": 1, "title": "Coconut Curry", "text": "coconut milk curry powder"},
    {"id": 2, "title": "Prawn Curry", "text": "prawn coconut curry isso"},
    {"id": 3, "title": "Dhal Curry", "text": "lentil curry coconut"},
    {"id": 4, "title": "Isso Curry", "text": "isso prawn spicy curry"},
    {"id": 5, "title": "Fish Ambul Thiyal", "text": "fish sour spicy goraka"},
]
def makeIndex(recipes):
    index={}
    for recipe in recipes:
        words=recipe['text'].split()
        for word in words:
            if word not in index:
                word=word.lower()#to make the search case insensitive
                index[word]=[]
            if recipe['id'] not in index[word]:
                index[word].append(recipe['id'])
    return index
indexes=makeIndex(recipes)
print(indexes)

def search_word(word,indexes):
    word=word.lower()#to make the search case insensitive
    return indexes.get(word,None)
 
def search_2_words(word1,word2,indexes):
    word1=word1.lower()#to make the search case insensitive
    word2=word2.lower()#to make the search case insensitive
    ids1=set(indexes.get(word1,None))
    ids2=set(indexes.get(word2,None))#if the word is not in the index, indexes.get will return None, and set(None) will be an empty set, which is what we want for the intersection to work correctly.
    if ids1 and ids2 :
        return list(ids1 & ids2)#lists dont have intersection but sets do
    elif ids1:
        return list(ids1)
    elif ids2:
        return list(ids2)
    else:
        return None
print(search_word("spicy", indexes))        # should return [4, 5]
print(search_2_words("prawn", "spicy", indexes))  # should return [4]
print(search_2_words("coconut", "curry", indexes)) # what do you expect here?