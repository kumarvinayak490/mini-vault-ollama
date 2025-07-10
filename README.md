# MiniVault API: Mini-ChatGPT

## Overview

This project uses Python and FastAPI to build the requested api `/generate`. The entire project uses docker to bring simplicity in setting it up so that it can be tested quickly. I assume the local system does not have ollama and I have created an image dedicated for that so that contained can be spawned from that. Stubbed response was easy and I thougt ollama will add this project with some weight. 

## Features

- **FastAPI Framework**: Clean, async-first Python API framework.
- **Single Endpoint**: `POST /generate` to simulate text generation.
- **Model-Based Response**: Mistral model is used in this project however we can edit to use any model.
- **Logging**: Logs each prompt and generated response to `logs/log.jsonl` (JSON Lines format).
- **Dockerized**: Uses Docker Compose to spin up the FastAPI app and Ollama in one command.

