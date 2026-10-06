from fastapi import FastAPI

from app.search import search_movies
from app.schemas import RecommendationResponse


app = FastAPI(
    title="Movie Recommendation API",
    description="Semantic movie recommendation API",
    version="1.0.0",
)


@app.get("/recommend", response_model=RecommendationResponse)
def recommend(query: str, top_k: int = 5):

    results = search_movies(query, top_k)

    recommendations = []

    for metadata, distance in zip(
        results["metadatas"][0],
        results["distances"][0],
    ):
        recommendations.append(
            {
                "title": metadata["title"],
                "distance": distance,
            }
        )

    return {
        "query": query,
        "recommendations": recommendations,
    }