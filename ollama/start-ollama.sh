#!/bin/sh
set -e

echo "[INFO] curl is installed and ready."

# Kill any previous Ollama process
pkill -f "ollama serve" 2>/dev/null || true

# Start Ollama in background
echo "[INFO] Starting Ollama server..."
ollama serve &

# Wait for it to become available
echo "[INFO] Waiting for Ollama API to become available..."
until curl -s http://localhost:11434 > /dev/null; do
  sleep 2
done

# Pull the model
MODEL="${OLLAMA_MODEL:-mistral}"
echo "[INFO] Pulling model: $MODEL..."
ollama pull "$MODEL" || { echo "[ERROR] Failed to pull model $MODEL"; exit 1; }

# Restart in foreground
pkill -f "ollama serve" 2>/dev/null || true
exec ollama serve
