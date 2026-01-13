#!/bin/bash

# Render deployment startup script
# This script starts the FastAPI server for Render deployment

echo "Starting FastAPI server on Render..."

# Start the server with Render's PORT environment variable or default to 8000
export PORT=${PORT:-8000}
export HOST=${HOST:-0.0.0.0}

python -m uvicorn app.main:app --host $HOST --port $PORT
