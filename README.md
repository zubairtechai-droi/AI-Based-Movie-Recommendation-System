# 🎬 AI Movie Recommendation System

A full-stack AI-powered movie recommendation system that recommends movies based on the **semantic meaning of movie descriptions**.

The project uses a free/open embedding model, `sentence-transformers/all-MiniLM-L6-v2`, to convert movie descriptions into vectors and uses **ChromaDB** for similarity search.

The application is built with **FastAPI**, **React**, and **Docker**, with movie metadata and posters retrieved from an online movie API.

> 🚧 **Project Status:** Initial development  
> This project will evolve over time as new AI, backend, database, and production features are added.

---

## 📌 Project Overview

The goal of this project is to build a simple but production-oriented recommendation system while learning how modern AI applications work.

A user provides a description of the type of movie they want.

For example:

> "I want a movie about astronauts trying to survive in space."

The system:

1. Receives the user's query.
2. Converts the query into an embedding.
3. Searches for semantically similar movie descriptions.
4. Returns the most relevant movies.
5. Displays the recommendations and movie posters in the React frontend.

### Basic Architecture

```text
                    ┌─────────────────┐
                    │   React Client  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │   REST API      │
                    └────────┬────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Recommendation Service  │
                └────────────┬────────────┘
                             │
                             ▼
                 ┌──────────────────────┐
                 │ Sentence Transformer │
                 │ all-MiniLM-L6-v2     │
                 └──────────┬───────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │  ChromaDB   │
                     │ Vector DB   │
                     └─────────────┘
```

---

# 🧠 How Recommendation Works

This is initially a **content-based recommendation system**.

We use the movie description as the main source of information.

```text
Movie Description
       │
       ▼
all-MiniLM-L6-v2
       │
       ▼
Embedding Vector
       │
       ▼
ChromaDB
       │
       ▼
Similarity Search
       │
       ▼
Recommended Movies
```

For example:

```text
Query:

"I want a movie about space survival."
```

The system converts the query into an embedding and compares it with the embeddings of movie descriptions.

Possible results:

```text
1. Interstellar
2. The Martian
3. Gravity
```

The system does **not** initially use:

- User profiles
- User ratings
- Collaborative filtering
- Complex recommendation algorithms

These may be added later.

---

# 🛠️ Technologies

## Backend

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

## AI / Machine Learning

- **Sentence Transformers**
- `sentence-transformers/all-MiniLM-L6-v2`
- Semantic embeddings
- Cosine/similarity-based retrieval

## Vector Database

- **ChromaDB**

## Frontend

- **React**
- JavaScript / TypeScript
- HTML
- CSS

## Data

- Online movie API
- Movie descriptions
- Movie posters
- Movie metadata

## DevOps

- **Docker**
- Docker Compose
- Git
- GitHub

---

# 📁 Project Structure

The project will gradually evolve, but the planned structure is:

```text
movie-recommender/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   └── routes/
│   │   │
│   │   ├── models/
│   │   │   └── embedding_model.py
│   │   │
│   │   ├── services/
│   │   │   └── recommender.py
│   │   │
│   │   └── database/
│   │       └── vector_store.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── Dockerfile
│
├── data/
│   └── README.md
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

The structure may change as the project grows.

---

# 🚀 Getting Started

## Prerequisites

Make sure you have installed:

- Python 3.10+
- Node.js 18+
- npm
- Git
- Docker Desktop

Check your versions:

```bash
python --version
node --version
npm --version
git --version
docker --version
```

---

# 🔧 Backend Setup

Go to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start React:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🐳 Running with Docker

The project will also support Docker so that the complete application can eventually be started with:

```bash
docker compose up --build
```

This will allow the backend, frontend, and supporting services to run in containers.

---

# 🔑 Environment Variables

API keys and secrets should **never be committed to GitHub**.

Create a local `.env` file:

```env
TMDB_API_KEY=your_api_key
```

An example environment file will be provided:

```text
.env.example
```

Example:

```env
TMDB_API_KEY=
```

The actual `.env` file should be included in `.gitignore`.

---

# 🔌 API

The initial API will be kept simple.

## Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

## Movie Recommendation

```http
POST /recommend
```

Request:

```json
{
  "query": "I want a movie about astronauts surviving in space"
}
```

Response:

```json
{
  "recommendations": [
    {
      "title": "Interstellar",
      "score": 0.89
    },
    {
      "title": "The Martian",
      "score": 0.84
    },
    {
      "title": "Gravity",
      "score": 0.81
    }
  ]
}
```

The exact API response will evolve as the project develops.

---




### 🔮 Future Ideas
Possible future improvements include:
- User Preferences — Let users select genres, themes, actors, or movie types they like.
- User Ratings — Allow users to rate movies they watched. These ratings can help improve future recommendations.
- Personalized Recommendations — Recommend movies based on each user's preferences, ratings, and previous interactions.
- Hybrid Recommendation — Combine description-based similarity with user ratings and other signals to produce better recommendations.
- PostgreSQL — Store application data such as users, movies, ratings, and recommendation history in a relational database.
- pgvector — Store and search movie embeddings directly inside PostgreSQL instead of using a separate vector database.
- Recommendation Ranking — Improve the order of results by combining similarity scores with ratings, popularity, genre, and other signals.
- Recommendation Explanations — Tell the user why a movie was recommended, for example: “Recommended because its story is similar to your search.”
- Authentication — Allow users to create accounts and securely manage their preferences, ratings, and recommendation history.
- Recommendation Analytics — Track things like searches, clicks, and which recommendations users actually choose to understand and improve the system.
- Cloud Deployment — Deploy the complete application online so anyone can use the recommendation system.

---

# 👨‍💻 Author

**Muhammad Zubair**

Building this project incrementally to explore practical AI engineering, recommendation systems, vector databases, backend development, and production deployment.
