## Overview

Project Description:

## Setup

Run `./setup.sh` to install dependencies and spin up the AppSec Pipeline services.

## Access services

StackStorm
* Container: `sudo docker exec -it stackstorm bash`
* UI: `localhost`

DefectDojo
* Container: `sudo docker exec -it banzaireal_dojo_1`
* UI: `localhost:8000`

## Data Persistence between local <-> containers

See `docker-compose.yml` in root folder to configure paths between local <-> containers

StackStorm Packs
* local: `./StackStorm/packs.dev`
* container: `./opt/stackstorm/packs.dev`
* Banzai-specific rules, actions, workflows are defined in packs.dev.
