#!/bin/bash

echo '============================================================'
echo '                    RUNNING DATAFETCH SERVER                '
echo '         This needs to run for the life of the pipeline     '
echo '============================================================'

# run datafetch script
sudo docker exec -it banzai_dojo_1 bash -c 'python findme/datafetch.py'
