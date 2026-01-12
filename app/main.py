from fastapi import FastAPI
from app.database import engine
from app.models import user, task
from app.routers import auth, tasks

app = FastAPI(
    title="Secure User Authentication & Task Management API",
    description="A FastAPI application with JWT authentication and task management",
    version="1.0.0"
)

user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Task Management API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
