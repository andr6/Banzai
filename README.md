# Banzai - AppSec Pipeline Project
====================================

### To-Do List

* Configure docker-compose.yml to include ToolChain services
* Script to perform POST request from DD -> SS, when a user creates a new Test from DD.

### Setup

__install dependencies__
* pip install defectdojo_api

__run environment__

* sudo docker-compose up

__local access to DefectDojo__

* localhost:8000

### Data Persistence

See docker-compose.yml for content that persists between local/containers.

__StackStorm Packs__
* local: ./StackStorm/packs.dev
* container: ./opt/stackstorm/packs.dev
* Banzai-specific rules, actions, workflows are defined in packs.dev.


## ISSUES ##

### StackStorm Container ###

A ToolChain install script 'toolchain_install.sh' from StackStorm/runtime/entrypoint.d is run upon container startup.
The script installs all security tools for use within the AppSec Pipeline, using the 'apt-get install' command.

If you have the NetworkManager daemon installed on your machine, go into the NetworkManager.conf file and comment out 'dns=dnsmasq' line.
The path to Networkmanager.conf should be '/etc/NetworkManager/NetworkManager.conf'

### Port Clashes ###

If a port number defined in the docker-compose.yaml is already being used by your host machine, docker-compose will fail to start up.
You must either stop the service on your local machine that is using the port, or change the port number in the docker-compose.yaml config file.

For more instructions on editing Docker Compose configuration files, please see: https://docs.docker.com/compose/overview/
