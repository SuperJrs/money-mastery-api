#!/bin/bash

docker exec -it money-mastery-api sh -c "cd ../tests && poetry run pytest . -rP"
# docker compose exec money-mastery-api poetry run pytest .
