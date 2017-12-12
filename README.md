# Banzai - AppSec Pipeline

Project Description:

## To-Do List

### DefectDojo <-> StackStorm Workflows
* Script to Poll DefectDojo MySQL db for new Test entries.
* Script to perform POST request, taking new Test data as the payload and sending it through to StackStorm via. its webhook. (sensor alternative)
* Script to upload test scan output from a StackStorm Action/Workflow to DD. `[COMPLETE]`
* Create StackStorm Action Chain to chain the test + import actions `[COMPLETE]`

### ToolChain Setup
NOTE: Explore ToolChain deployment outside of SS container.
* Install NMAP within StackStorm container `[COMPLETE]`
* Install ZAP within StackStorm container
* Install Burp within StackStorm container
* Install Nessus within StackStorm container
* Install Veracode within StackStorm container

### Testing + Exceptions
* Set up local gruyere instance deployed via. Docker `[COMPLETE]`
* Exception handling for failed action: DefectDojo import
* Exception handling for failed action: request to StackStorm webhook API
* Exception handling for failed action: execute Nmap test scan

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
Docker Containers must be within the same network to be able to talk to each other. When Docker spins up containers, it assigns each container to the default bridge network. Due to the AppSec Pipeline setup, some services within the pipeline connect to a different default bridge network. For example, the StackStorm container will be on a different network, so you must manually connect it to the main `banzaireal_default` bridge network.

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

### Docker-Compose Network Bridge ###

Docker adds containers to a "default bridge network" when they are first run. Due to the Banzai implementation, the StackStorm container will be connected to a separate bridge network than the DefectDojo container. To solve this issue, you must use the command `sudo docker network connect [NETWORK_NAME] [CONTAINER]` to connect your StackStorm container to the network that DefectDojo belongs to, so they can communicate.

See more about Docker Networking here: https://docs.docker.com/engine/userguide/networking/

### Port Clashes ###

If a port number defined in the docker-compose.yaml is already being used by a running application on your host machine, docker-compose will fail to start up.
You must either stop the application that is using the port, or change the port number in the docker-compose.yaml config file to an unused port number.

For more instructions on editing Docker Compose configuration files, please see: https://docs.docker.com/compose/overview/
