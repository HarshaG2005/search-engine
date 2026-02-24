import os
import sys

# Ensure project root is on sys.path when this file is executed directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercises.ex1 import indexes
# def getGrams(word):
#     grams=[]
#     for i in range(len(word)):
#         if i==len(word)-1:
#             return grams

#         gram=word[i:i+2]
#         grams.append(gram)
#     return grams

def get_bigrams(word):
    word = word.lower()
    return [word[i:i+2] for i in range(len(word)-1)]

def build_bigram_index(indexes):
    bigram_index = {}
    for word in indexes.keys():
        bigrams = get_bigrams(word)
        for bigram in bigrams:
            if bigram not in bigram_index:
                bigram_index[bigram] = []
            if word not in bigram_index[bigram]:
                bigram_index[bigram].append(word)
    return bigram_index
bigram_index = build_bigram_index(indexes)

def get_candidates(misspelled, bigram_index):
    bigrams = get_bigrams(misspelled)
    
    candidates = {}
    for bigram in bigrams:
        matches = bigram_index.get(bigram, [])
        for word in matches:
            if word not in candidates:
                candidates[word] = 0
            candidates[word] += 1  # count shared bigrams
    
    # sort by most shared bigrams
    return sorted(candidates.items(), key=lambda x: x[1], reverse=True)
# Example usage:
misspelled_word = "cari"    
# candidates = get_candidates(misspelled_word, bigram_index)
# print(candidates)
