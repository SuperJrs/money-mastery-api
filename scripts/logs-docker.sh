#!/bin/bash

# Comando para visualizar log de um container, tenso em conta que $1 é o nome do container
docker logs -f $1
