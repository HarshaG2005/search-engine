from pathlib import Path
import json

out_dir = Path("index_data")
out_dir.mkdir(exist_ok=True)
def save(index,doc_len,avg_doc_len,recipe_map):
    (out_dir/ "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2 ,default=list), encoding="utf-8")
    (out_dir/ "doc_len.json").write_text(json.dumps(doc_len, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir/ "avg_doc_len.json").write_text(json.dumps(avg_doc_len, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir/ "recipe_map.json").write_text(json.dumps(recipe_map, ensure_ascii=False, indent=2), encoding="utf-8")

def load():
    if not (out_dir / "index.json").exists():
        raise FileNotFoundError("Index not built yet — run indexer.py first")
    index = json.loads((out_dir/ "index.json").read_text(encoding="utf-8"))
    doc_len = json.loads((out_dir/ "doc_len.json").read_text(encoding="utf-8"))
    avg_doc_len = json.loads((out_dir/ "avg_doc_len.json").read_text(encoding="utf-8"))
    recipe_map = json.loads((out_dir/ "recipe_map.json").read_text(encoding="utf-8"))   
    return index, doc_len, avg_doc_len, recipe_map
def load_recipe():
    with open(Path("data/recipe.json"), encoding="utf-8") as f:
        recipes = json.load(f)
    return recipes