# minivault-api/app.py

import json
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama 


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.jsonl")


OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434") # Default Ollama API endpoint

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")


app = FastAPI(
    title="MiniVault API (with Ollama)",
    description=f"A lightweight local REST API simulating a text generation system, powered by Ollama ({OLLAMA_MODEL}).",
    version="1.0.0",
)

class GenerateRequest(BaseModel):
    """
    Request model for the /generate endpoint.
    """
    prompt: str
    
    model: str = OLLAMA_MODEL

class GenerateResponse(BaseModel):
    """
    Response model for the /generate endpoint.
    """
    response: str


def log_interaction(prompt: str, response: str):
    """
    Logs the prompt and its corresponding response to a JSON Lines file.
    Ensures the log directory exists before writing.
    """
  
    os.makedirs(LOG_DIR, exist_ok=True)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    except IOError as e:
        print(f"Error writing to log file {LOG_FILE}: {e}")


@app.post("/generate", response_model=GenerateResponse, summary="Generate Text with Ollama")
async def generate_text(request: GenerateRequest):
    """
    Generates text using a local Ollama model.
    Logs every prompt and its response.
    """
    prompt = request.prompt
    model_to_use = request.model 

    print(f"Received prompt: '{prompt}' for model: '{model_to_use}'")

    generated_text = ""
    try:
        
        client = ollama.Client(host=OLLAMA_HOST)

        
        response_ollama = client.generate(model=model_to_use, prompt=prompt)
        generated_text = response_ollama['response']

    except ollama.ResponseError as e:
        print(f"Ollama API Error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error from Ollama API: {e.error}"
        )
    except ollama.RequestError as e:
        print(f"Ollama Connection Error: {e}")
        raise HTTPException(
            status_code=503,
            detail=f"Could not connect to Ollama server at {OLLAMA_HOST}. Is Ollama running and model '{model_to_use}' downloaded?"
        )
    except Exception as e:
        print(f"An unexpected error occurred during text generation: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {e}"
        )

  
    log_interaction(prompt, generated_text)

    return GenerateResponse(response=generated_text)


@app.get("/", summary="API Health Check")
async def root():
    """
    Basic health check endpoint for the API.
    """
    return {"message": "MiniVault API is running!"}