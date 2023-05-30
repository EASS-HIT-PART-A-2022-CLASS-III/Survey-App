import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from io import StringIO

app = FastAPI()

# Allow requests from http://localhost:8000
origins = [
    "http://localhost:8000",
]

# Add the CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a stream handler to capture logs in memory
log_stream = StringIO()
stream_handler = logging.StreamHandler(log_stream)

# Configure the logger
logging.basicConfig(level=logging.INFO, handlers=[stream_handler])

@app.get("/log")
async def get_logs():
    log_messages = log_stream.getvalue().splitlines()
    return {"logs": log_messages}

@app.post("/log")
async def log_message(payload: dict):
    message = payload.get("message")
    if message:
        print(message)
        logging.info(message)
        return {"message": "Logged successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid payload format")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
