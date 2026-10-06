from sentence_transformers import SentenceTransformer

from data.movies import movies


# Load the embedding model.
# MiniLM converts text into 384-dimensional vectors.
model = SentenceTransformer("all-MiniLM-L6-v2")



"""
    Generate an embedding for every movie description.
"""
def generate_movie_embeddings():

    descriptions = [movie["description"] for movie in movies]

    embeddings = model.encode(descriptions)

    return embeddings


if __name__ == "__main__":
    embeddings = generate_movie_embeddings()

    print("Number of movies:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))

    print("\nFirst movie:")
    print(movies[0]["title"])

    #print("\nFirst movie embedding:")
    #print(embeddings[0])