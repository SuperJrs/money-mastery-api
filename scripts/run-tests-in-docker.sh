#!/bin/bash

docker exec -it money-mastery-api sh -c "cd ../tests && poetry run pytest . -s"
# docker compose exec money-mastery-api poetry run pytest .
