# MiniVault API: Mini-ChatGPT

## Overview

This project implements a lightweight REST API using **Python** and **FastAPI** with a single `/generate` endpoint to simulate text generation. The entire application is **containerized using Docker**, making it easy to set up and run locally without requiring manual installation of dependencies like Ollama or any models.

While the stubbed response was simple to implement, this project also integrates a local LLM using **Ollama** and the **Mistral** model to enhance realism and demonstrate local model usage without relying on cloud APIs.

## Features

* ⚡ **FastAPI**: Modern, async-first web framework for building APIs in Python.
* 🔥 **Single Endpoint**: `POST /generate` for prompt-based text generation.
* 🧠 **Local LLM Integration**: Uses the **Mistral** model via Ollama (easily switchable to others like LLaMA2).
* 📄 **Logging**: All prompts and their generated responses are logged in `logs/log.jsonl` using JSON Lines format.
* 🐳 **Dockerized**: Includes a `docker-compose.yml` for easy setup of both the API and Ollama containers.

---

## Installation

> 🛠 **Prerequisite**: Docker must be installed on your machine.

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/minivault-api.git
   ```

2. **Navigate into the project directory**

   ```bash
   cd minivault-api
   ```

3. **Make the startup script executable**

   ```bash
   chmod +x ollama/start-ollama.sh
   ```

4. **Start the project using Docker Compose**

   ```bash
   docker compose up
   ```

> ⚠️ The initial setup may take **5–10 minutes**, as the Ollama container pulls and prepares the model.

---

## Testing the API

You can test the `/generate` endpoint using `curl`:

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me a fun fact about llamas."}'
```

---

## Future Improvements

* 🔧 **Code Structure**: The current implementation keeps everything in a single file for simplicity. For a production-grade application, the project can be modularized using a layered architecture (e.g., **Controller-Service-Repository**).
* 🤖 **Model Selection**: The current setup uses the **Mistral** model to reduce download/setup time. It can be easily updated to use **LLaMA2** or any other Ollama-compatible model by modifying the Docker environment or startup script.

---
