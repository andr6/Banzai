## Overview

The aim of the AppSec pipeline is to provide the ability to perform automated security assessments against a system. The pipeline should help reduce the amount of time spent on repetitive AppSec activities, to optimise use of a security team. It should also be a tool that can serve as a consistent process which can be followed by security teams.

## Setup

1. Run `./setup.bash` to setup the pipeline and start a webhook service. This process must be kept running throughout the life of the pipeline.
2. Access the `Burpdock` container by running `sudo docker exec -it burpdock bash`
3. Inside the container, navigate to `opt/burpdock/burp-rest-api` and run `java -jar build/libs/burp-rest-api-1.0.0.jar` to launch the Burp Rest API service. You will be prompted to enter your Burp Professional license. Keep this proces running throughout the life of the pipeline.

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
