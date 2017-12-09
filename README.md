\# Banzai - AppSec Pipeline Project


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

### To-Do List ###

* Configure docker-compose.yml to include ToolChain services
* Script to perform POST request from DD -> SS, when a user creates a new Test from DD.

### StackStorm Container Issues ###

A ToolChain install script 'toolchain_install.sh' from StackStorm/runtime/entrypoint.d is run upon container startup.
The script installs all security tools for use within the AppSec Pipeline, using the 'apt-get install' command.

If you have the NetworkManager daemon installed on your machine, go into the NetworkManager.conf file and comment out 'dns=dnsmasq' line.
The path to Networkmanager.conf should be '/etc/NetworkManager/NetworkManager.conf'
