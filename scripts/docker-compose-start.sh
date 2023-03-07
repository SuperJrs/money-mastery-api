#!/bin/bash

# Verifica se o Docker Compose está instalado
if command -v docker compose &> /dev/null; then
    docker compose up -d
elif command -v docker-compose &> /dev/null; then
    docker-compose up -d
else
    echo "O Docker Compose não está instalado. Instale-o e tente novamente."
    exit 1
fi

