# Banzai - AppSec Pipeline

Project Description:

## To-Do List

### Connect DefectDojo with StackStorm
* Script to perform POST request from DD -> SS, when a user creates a new Test from DD.

### ToolChain Setup
NOTE: Explore ToolChain deployment outside of SS container.
* Install ZAP within StackStorm container
* Install Burp within StackStorm container
* Install Nessus within StackStorm container
* Install Veracode within StackStorm container

## Setup

install dependencies
* `pip install defectdojo_api`

run environment
* `sudo docker-compose up`

browser access to DefectDojo
* `localhost:8000`

browser access to StackStorm GUI
* `localhost`

## Docker Network Setup

Connect containers to the same Docker bridge network
* sudo docker network connect [default_bridge_name] [container_name]

## Data Persistence

See docker-compose.yml for content that persists between your local machine / containers.

__StackStorm Packs__
* local: `./StackStorm/packs.dev`
* container: `./opt/stackstorm/packs.dev`
* Banzai-specific rules, actions, workflows are defined in packs.dev.

## Issues ##

### StackStorm Container: apt-get install ###

A ToolChain install script `toolchain_install.sh` from `StackStorm/runtime/entrypoint.d` is run upon container startup.
The script installs all security tools for use within the AppSec Pipeline, using the 'apt-get install' command.

If you have the NetworkManager daemon installed on your machine, go into the `NetworkManager.conf` file and comment out `dns=dnsmasq` line.
The path to Networkmanager.conf should be `/etc/NetworkManager/NetworkManager.conf`

OS tested with issues:
* Ubuntu 16.04

OS tested without issues:
* MacOS High Sierra

### Port Clashes ###

If a port number defined in the docker-compose.yaml is already being used by a running application on your host machine, docker-compose will fail to start up.
You must either stop the application that is using the port, or change the port number in the docker-compose.yaml config file to an unused port number.

For more instructions on editing Docker Compose configuration files, please see: `https://docs.docker.com/compose/overview/`
