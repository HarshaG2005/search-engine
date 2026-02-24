from nltk.metrics.distance import edit_distance
from kGram import get_candidates, bigram_index
from exercises.ex1 import indexes
from nltk.stem import PorterStemmer
ps = PorterStemmer()
def spell_correct(query, bigram_index, indexes, threshold=2):
    # step 1 - check if word exists in index already
    query = query.lower()
    query = ps.stem(query)
    if query in indexes:
        return query  # no correction needed
    
    # step 2 - get candidates from bigram index
    candidates = get_candidates(query, bigram_index)
    
    # step 3 - confirm with edit distance
    best_match = None
    best_distance = float('inf')
    
    for candidate, shared_bigrams in candidates:
        distance = edit_distance(query, candidate)
        if distance < best_distance and distance <= threshold:
            best_distance = distance
            best_match = candidate
    
    return best_match if best_match else query
print(spell_correct("cocnut", bigram_index, indexes))    # coconut
print(spell_correct("prwan", bigram_index, indexes))     # prawn
print(spell_correct("spicy", bigram_index, indexes))     # spicy (no correction needed)