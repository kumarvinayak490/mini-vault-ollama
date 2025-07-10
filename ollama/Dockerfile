
FROM ollama/ollama:latest

RUN apt-get update && \
    apt-get install -y curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY ./ollama/start-ollama.sh /start-ollama.sh
RUN chmod +x /start-ollama.sh

# These lines can be removed if you don't need to add custom certificates
# As I was behind proxy, I had to add custom certificates
COPY ./certs/*.pem /usr/local/share/ca-certificates/
RUN \
  for f in /usr/local/share/ca-certificates/*.pem; do \
    cp "$f" "${f%.pem}.crt"; \
  done && \
  update-ca-certificates

  
ENTRYPOINT ["/bin/sh", "-c", "/start-ollama.sh"]
