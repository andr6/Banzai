## Overview

Project Description:

## Setup

install dependencies
* `pip install defectdojo_api`

run environment
* `sudo docker-compose up`

## Access services

StackStorm
* Container: `sudo docker exec -it stackstorm bash`
* UI: `localhost`

DefectDojo
* Container: `sudo docker exec -it banzaireal_dojo_1`
* UI: `localhost:8000`

## Data Persistence between local <-> containers

See docker-compose.yml for content that persists between your local machine / containers.

StackStorm Packs
* local: `./StackStorm/packs.dev`
* container: `./opt/stackstorm/packs.dev`
* Banzai-specific rules, actions, workflows are defined in packs.dev.
