from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "server": "B",
        "host": socket.gethostname(),
        "status": "healthy"
    }

@app.get("/health")
def health():
    return {"status": "ok"}