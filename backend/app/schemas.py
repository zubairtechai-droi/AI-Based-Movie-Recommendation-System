from pydantic import BaseModel


class MovieRecommendation(BaseModel):
    title: str
    distance: float


class RecommendationResponse(BaseModel):
    query: str
    recommendations: list[MovieRecommendation]