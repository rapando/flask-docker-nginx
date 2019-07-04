#!/usr/bin/env bash
pipenv lock -r > requirements.txt
docker-compose build
docker-compose up
rm requirements.txt