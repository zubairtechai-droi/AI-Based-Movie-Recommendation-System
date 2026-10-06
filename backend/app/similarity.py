import numpy as np

from app.embeddings import model, generate_movie_embeddings
from data.movies import movies


def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.
    """

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


def recommend_movies(query, top_k=5):
    """
    Find movies whose descriptions are most similar
    to the user's query.
    """

    # Generate embeddings for all movies
    movie_embeddings = generate_movie_embeddings()

    # Convert user's query into an embedding
    query_embedding = model.encode(query)

    # Calculate similarity with every movie
    results = []

    for movie, movie_embedding in zip(movies, movie_embeddings):
        score = cosine_similarity(query_embedding, movie_embedding)

        results.append({
            "title": movie["title"],
            "score": float(score)
        })

    # Sort from highest similarity to lowest
    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]


if __name__ == "__main__":
    query = "I want a movie about surviving in space."

    recommendations = recommend_movies(query)

    print("\nQuery:")
    print(query)

    print("\nRecommendations:")

    for movie in recommendations:
        print(f'{movie["title"]}: {movie["score"]:.4f}')