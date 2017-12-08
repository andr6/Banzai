# Banzai - AppSec Pipeline Project


### Setup

__install dependencies__
pip install defectdojo_api

__run environment__
sudo docker-compose up

__local access to DefectDojo__
localhost:8000

### Data Persistence

See docker-compose.yml for content that persists between local/containers.


__StackStorm Packs__
local: ./StackStorm/packs.dev
container: ./opt/stackstorm/packs.dev
* Banzai-specific rules, actions, workflows are defined in packs.dev.

NOTE: See docker-compose.yml for 

### TO-DO LIST ###

* Configure docker-compose.yml to include ToolChain services
* Script to perform POST request from DD -> SS, when a user creates a new Test from DD.
