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