from nltk.metrics.distance import edit_distance
from core.preprocesser import preprocess

def get_bigrams(word):
    """Generate bigrams from a word."""
    word = word.lower()
    return [word[i : i + 2] for i in range(len(word) - 1)]


def build_bigram_index(indexes):
    """Builds a bigram index from the existing term index."""
    bigram_index = {}
    for word in indexes.keys():
        bigrams = get_bigrams(word)
        for bigram in bigrams:
            if bigram not in bigram_index:
                bigram_index[bigram] = []
            if word not in bigram_index[bigram]:
                bigram_index[bigram].append(word)
    return bigram_index

def get_candidates(misspelled,indexes):
    """Get candidate corrections based on shared bigrams."""
    bigrams = get_bigrams(misspelled)
    bigram_index = build_bigram_index(indexes)  # build bigram index from current term index
    candidates = {}
    for bigram in bigrams:
        matches = bigram_index.get(bigram, [])
        for word in matches:
            if word not in candidates:
                candidates[word] = 0
            candidates[word] += 1  # count shared bigrams

    # sort by most shared bigrams
    return sorted(candidates.items(), key=lambda x: x[1], reverse=True)




def spell_correct(query,indexes, threshold=2):
    """Corrects a misspelled query term using bigram candidates and edit distance."""
    # step 1 - check if word exists in index already
    # preprocess and take the first word (assuming single word input)
    if query in indexes:
        return query  # no correction needed

    # step 2 - get candidates from bigram index
    candidates = get_candidates(query, indexes)

    # step 3 - confirm with edit distance
    best_match = None
    best_distance = float("inf")

    for candidate, shared_bigrams in candidates:
        distance = edit_distance(query, candidate)
        if distance < best_distance and distance <= threshold:
            best_distance = distance
            best_match = candidate

    return best_match if best_match else query


def transform(raw_query,indexes):
    tokens = preprocess(raw_query)        # ["chiken", "cocnut", "curi"]
    
    corrected = []
    for token in tokens:
        fixed = spell_correct(token, indexes) # one token at a time
        corrected.append(fixed)
    
    return corrected     
