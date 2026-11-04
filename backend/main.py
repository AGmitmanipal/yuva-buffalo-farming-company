from fastapi import FastAPI

from routers import buffalo

app = FastAPI(
    title="Yuva Buffalo Farming API",
    description="API for managing buffalo farms and dairy operations",
    version="1.0.0"
)

app.include_router(buffalo.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Yuva Buffalo Farming Company!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

