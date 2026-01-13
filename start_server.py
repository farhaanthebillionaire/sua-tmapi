import subprocess
import webbrowser
import time
import threading
from pathlib import Path

def start_server():
    """Start the FastAPI server"""
    try:
        subprocess.run([
            "python", "-m", "uvicorn", 
            "app.main:app", 
            "--reload", 
            "--host", "127.0.0.1", 
            "--port", "8000"
        ], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped by user")

def open_docs():
    """Wait a moment for server to start, then open docs"""
    time.sleep(2)  # Wait for server to start
    webbrowser.open("http://127.0.0.1:8000/docs")
    print("Opening API documentation at http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    print("Starting FastAPI server...")
    
    # Start server in background thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Open docs after a short delay
    open_docs()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
