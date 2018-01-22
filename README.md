## Overview

The aim of the AppSec pipeline is to provide the ability to perform automated security assessments against a system. The pipeline should help reduce the amount of time spent on repetitive AppSec activities, to optimise use of a security team. It should also be a tool that can serve as a consistent process which can be followed by security teams.

## Setup

1. Run `./startup.bash` to setup the pipeline and start a webhook service. This process must be kept running throughout the life of the pipeline.
2. Access the `Burpdock` container by running `sudo docker exec -it burpdock bash`
3. Inside the container, run `java -jar opt/burpdock/burp-rest-api/build/libs/burp-rest-api-1.0.0.jar` to launch the Burp Rest API service. You will be prompted to enter your Burp Professional license. Keep this process running throughout the life of the pipeline.

## Access services

StackStorm
* Container: `sudo docker exec -it stackstorm bash`
* UI: `localhost`

DefectDojo
* Container: `sudo docker exec -it banzaireal_dojo_1 bash`
* UI: `localhost:8000`

Burp Rest API
* Container: `sudo docker exec -it burpdock bash`

Google Gruyere
* Container: `sudo docker exec -it gruyere bash`
* UI: localhost:8008

## Data Persistence between local host <-> containers

See `docker-compose.yml` in Banzai root folder to configure paths between local <-> containers.

DefectDojo datafetch script
* What: Script to poll DefectDojo's database for new test scans and send a request to StackStorm to trigger a scan workflow.
* Local dir: `./DefectDojo/findme/datafetch.py`
* Container dir: `./opt/django-DefectDojo/findme/datafetch.py`

StackStorm Packs
* What: StackStorm rules, actions and workflow configuration for the AppSec pipeline.
* Local dir: `./StackStorm/packs.dev`
* Container dir: `./opt/stackstorm/packs.dev`
* Help: To configure StackStorm automation, read more at `https://docs.stackstorm.com`

Test scan results
* What: Storage of test scan results for Nmap, Burp, Nessus and Fortify. Used by pipeline to import results into the DefectDojo platform.
* Local dir: `./scan_results
* Container dir: `./opt/stackstorm/scan_results`

Common environment variables
* What: A folder containing shared environment variables used between the pipeline containers.
* Local dir: `./common`
* StackStorm container dir: `opt/stackstorm/common`
* DefectDojo container dir: `opt/django-DefectDojo/common`
