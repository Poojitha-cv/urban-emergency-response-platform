from fastapi import FastAPI

app = FastAPI(
    title="Urban Emergency Response Platform",
    version="1.0.0",
    description="Backend API for the Urban Emergency Response & Incident Management Platform"
)


@app.get("/")
def root():
    return {
        "message": "Urban Emergency Response Platform API is running."
    }