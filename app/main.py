from fastapi import FastAPI
from core.indexer import build_index
from core.search import search
from core.storage import load_recipe
from app.schema import SearchRequest, RecipeResult, SearchResponse
app = FastAPI(title="CurryScope API")

@app.get("/search", response_model=SearchResponse)
def search_recipes(query: str, top_k: int = 5):
    results = search(query, top_k=top_k)
    return SearchResponse(query=query, results=results)