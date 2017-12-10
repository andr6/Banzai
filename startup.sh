#!/bin/bash

# install defefectdojo python module
echo 'y' | pip install defectdojo_api

# spin up docker containers
echo
echo 'If Docker Compose is already installed on your host machine, you can start the AppSec Pipeline with the command:'
echo '$ sudo docker-compose up'
