from pathlib import Path
import json

out_dir = Path("index_data")
out_dir.mkdir(exist_ok=True)
def save(index,doc_len,avg_doc_len):
    (out_dir/ "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir/ "doc_len.json").write_text(json.dumps(doc_len, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir/ "avg_doc_len.json").write_text(json.dumps(avg_doc_len, ensure_ascii=False, indent=2), encoding="utf-8")

