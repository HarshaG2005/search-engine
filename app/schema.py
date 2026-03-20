from pydantic import BaseModel, ConfigDict
from typing import List

class SearchRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # strips spaces from "  chicken  " → "chicken"
        str_min_length=1,           # rejects empty string queries ""
    )
    query: str
    top_k: int = 5

class RecipeResult(BaseModel):
    model_config = ConfigDict(
        from_attributes=True        # can read from objects, not just dicts
    )
    title: str
    score: float
    img_url: str = ""
    url: str = ""

class SearchResponse(BaseModel):
    query: str
    results: List[RecipeResult]
