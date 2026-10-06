from fastapi import FastAPI


# Create the FastAPI application
app = FastAPI(
    title="AI Movie Recommendation System",
    version="1.0.0"
)


# Health check endpoint
# Used to verify that the API is running
@app.get("/health")
def health():
    return {"status": "ok"}