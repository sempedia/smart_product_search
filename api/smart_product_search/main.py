from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import httpx
import spacy
import re
from difflib import SequenceMatcher

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache


app = FastAPI()

# Allow React frontends to call API in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: dict


class SearchResponse(BaseModel):
    results: List[Product]


def parse_query(text: str):
    """
    Parse search query to extract:
    - keywords
    - max_price
    - min_rating
    Handles "$", "under", "less than", and plain numbers.
    """
    doc = nlp(text.lower())
    keywords = []
    max_price = None
    min_rating = None

    for token in doc:
        if token.pos_ in ("NOUN", "ADJ") and not token.is_stop:
            lemma = token.lemma_.lower()
            keywords.append(lemma)

    # Normalize some common plurals or variants manually
    plural_map = {
        "men": "man",
        "mens": "man",
        "women": "woman",
        "womens": "woman",
        "children": "child",
        "kids": "child",
        "geese": "goose",
        # Add more if you want
    }

    # Apply mapping
    normalized_keywords = [plural_map.get(kw, kw) for kw in keywords]

    # Detect money entity via spaCy
    for ent in doc.ents:
        if ent.label_ == "MONEY":
            price_str = re.sub(r"[^\d.]", "", ent.text)
            if price_str:
                max_price = float(price_str)

    # Fallback: detect patterns like "under $100" or "less than 50"
    if max_price is None:
        # regex explanation:
        # Optional "under" or "less than" phrase + optional whitespace + optional $ + number with optional decimal
        price_match = re.search(r"(?:under|less than)?\s*\$?(\d+(?:\.\d{1,2})?)", text.lower())
        if price_match:
            max_price = float(price_match.group(1))

    if "good reviews" in text.lower() or "high rating" in text.lower():
        min_rating = 4

    return normalized_keywords, max_price, min_rating


def is_fuzzy_match(keyword: str, text: str, threshold=0.7) -> bool:
    """Check if keyword is similar enough to any word in the text."""
    for word in text.split():
        if SequenceMatcher(None, keyword, word).ratio() >= threshold:
            return True
    return False


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


@app.get("/smart-product-search", response_model=SearchResponse)
@cache(expire=60)
async def smart_product_search(
    query: str = Query(..., min_length=1),
    max_price: Optional[float] = Query(None, alias="maxPrice"),
    category: Optional[str] = None,
):
    keywords, parsed_max_price, min_rating = parse_query(query)
    keywords = set(keywords)  # convert to set for faster membership test

    # Remove automatic category override based on keywords
    # So category filter applies only if category param is set by user

    effective_max_price = max_price if max_price is not None else parsed_max_price

    url = "https://fakestoreapi.com/products"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch products")
        products = response.json()

    filtered = []
    for p in products:
        title_lower = p["title"].lower()
        desc_lower = p["description"].lower()
        product_category = p["category"].lower()

        title_doc = nlp(title_lower)
        desc_doc = nlp(desc_lower)
        title_lemmas = {token.lemma_ for token in title_doc if not token.is_stop and token.is_alpha}
        desc_lemmas = {token.lemma_ for token in desc_doc if not token.is_stop and token.is_alpha}

        if keywords:
            keyword_match = False
            for kw in keywords:
                if (
                    kw in title_lemmas
                    or kw in desc_lemmas
                    or kw in title_lower
                    or kw in desc_lower
                    or is_fuzzy_match(kw, title_lower)
                    or is_fuzzy_match(kw, desc_lower)
                ):
                    keyword_match = True
                    break
            if not keyword_match:
                continue

        # Filter by max price (if set)
        if effective_max_price is not None and p["price"] > effective_max_price:
            continue

        # Filter by category ONLY if user set category explicitly
        if category and category.lower() != product_category:
            continue

        # Filter by min rating (if set)
        if min_rating is not None and p["rating"]["rate"] < min_rating:
            continue

        filtered.append(p)

    return {"results": filtered}
