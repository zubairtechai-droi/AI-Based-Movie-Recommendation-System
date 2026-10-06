import chromadb

from app.embeddings import generate_movie_embeddings
from data.movies import movies


# Create a local ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")


# Create or get our movie collection
collection = client.get_or_create_collection(
    name="movies"
)


def store_movies():
    """
    Generate embeddings and store movies in ChromaDB.
    """

    # Generate embeddings for all movies
    embeddings = generate_movie_embeddings()

    # Store movies in ChromaDB
    collection.add(
        ids=[str(movie["id"]) for movie in movies],
        embeddings=embeddings.tolist(),
        documents=[movie["description"] for movie in movies],
        metadatas=[
            {"title": movie["title"]}
            for movie in movies
        ]
    )

    print(f"Stored {len(movies)} movies in ChromaDB.")


if __name__ == "__main__":
    store_movies()