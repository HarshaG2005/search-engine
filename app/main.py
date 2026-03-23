from fastapi import FastAPI
from core.indexer import build_index
from core.search import search
from core.storage import load_recipe
from app.schema import SearchRequest, RecipeResult, SearchResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="CurryScope API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/search", response_model=SearchResponse)
def search_recipes(q: str, top_k: int = 5):
    results = search(q, top_k=top_k)
    return SearchResponse(query=q, results=results)
