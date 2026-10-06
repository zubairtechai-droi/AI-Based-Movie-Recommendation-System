import chromadb

from app.embeddings import model


# Connect to our existing ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get our existing collection
collection = client.get_collection("movies")


def search_movies(query, top_k=5):
    """
    Search for movies semantically similar to the user's query.
    """

    # Convert the user's query into a vector
    query_embedding = model.encode(query).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":

    query = "I want a movie about surviving in space."

    results = search_movies(query)

    print("\nQuery:")
    print(query)

    print("\nRecommendations:")

    for title, distance in zip(
        results["metadatas"][0],
        results["distances"][0]
    ):
        print(
            f'{title["title"]}: distance={distance:.4f}'
        )