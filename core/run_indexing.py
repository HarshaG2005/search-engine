from core.indexer import build_index
from core.storage import load_recipe, save


def run_indexing():
    recipes = load_recipe()
    indexes, doc_len, recipe_map, bigram_index,doc_field_len,avg_field_len = build_index(recipes)
    avg_doc_len = sum(doc_len.values()) / len(doc_len) if doc_len else 0
    # dfs = {term: len(i[term].keys) for term, i in indexes.items()}
    save(indexes, doc_len, avg_doc_len, recipe_map, bigram_index,doc_field_len,avg_field_len)
    return True


if __name__ == "__main__":
    run_indexing()
    print("Indexing completed successfully.")
