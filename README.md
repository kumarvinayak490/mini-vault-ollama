# MiniVault API: Mini-ChatGPT

## Overview

This project uses Python and FastAPI to build the requested api `/generate`. The entire project uses docker to bring simplicity in setting it up so that it can be tested quickly. I assume the local system does not have ollama and I have created an image dedicated for that so that contained can be spawned from that. Stubbed response was easy and I thougt ollama will add this project with some weight. 

## Features

- **FastAPI Framework**: Clean, async-first Python API framework.
- **Single Endpoint**: `POST /generate` to simulate text generation.
- **Model-Based Response**: Mistral model is used in this project however we can edit to use any model.
- **Logging**: Logs each prompt and generated response to `logs/log.jsonl` (JSON Lines format).
- **Dockerized**: Uses Docker Compose to spin up the FastAPI app and Ollama in one command.

### Installation

The setup would require the host system to have docker installed. Please ensure the docker is installed and it will need just one command to run the project. Also, while setting up the ollama container, pulling the model from the registery takes some time, so please allow some time for the entire installation to finish which would take about 5-10 minutes.

1.  **Clone the repository:**
    
2.  **Navigate to the project directory:**

    ```bash
    cd minivault-api
    ```
2.  **Allow permission to the script file:**

    ```bash
    chmod +x ollama/start-ollama.sh
    ```

3.  **Run the docker compose command:**

   ```bash
    docker compose up
    ```

### Testing

Use the curl command below to test:

 ```bash
    curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me a fun fact about llamas."}'
```


### Future Improments

Currently, the project uses just one file to contain the apis however as we do it one production, we can use Controller, Repository, Services architecture to modularise each piece of the fucntionality as required. This project is built for simplicity. Also, the model that I have used is mistral instead of llama2 which would have taken a lot of time to setup. 





