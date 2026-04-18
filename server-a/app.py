from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import socket

app = FastAPI()

REQUESTS = Counter("app_requests_total", "Total Requests")

@app.get("/")
def home():
    REQUESTS.inc()
    return {
        "server": "A",
        "host": socket.gethostname(),
        "status": "healthy"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")