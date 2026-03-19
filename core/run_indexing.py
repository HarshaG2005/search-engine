from core.indexer import build_index
from core.storage import load_recipe, save


def run_indexing():
    recipes = load_recipe()
    indexes, doc_len, recipe_map, bigram_index = build_index(recipes)
    avg_doc_len = sum(doc_len.values()) / len(doc_len) if doc_len else 0
    save(indexes, doc_len, avg_doc_len, recipe_map, bigram_index)
    return True


if __name__ == "__main__":
    run_indexing()
    print("Indexing completed successfully.")
