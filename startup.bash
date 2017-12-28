#!/bin/bash
echo '============================================================'
echo '                  LAUNCHING APPSEC PIPELINE                 '
echo '============================================================'

# spin up Docker containers
sudo docker-compose up -d
echo '... Docker containers created'

echo
echo '============================================================'
echo '               SETTING UP PIPELINE VARIABLES                '
echo '============================================================'

# remove old variables
> common/networks.txt
> common/api_keys.txt
echo '... Old variables removed successfully'

# get StackStorm container IP (for use by DefectDojo)
ss_key="SS_IP="
ss_value=$(sudo docker network inspect banzai_default | grep -A 3 'stackstorm' | grep 'IPv4' | sed 's/.*: "//' | sed 's/\/.*//')
ss_ip=$ss_key$ss_value
echo $ss_ip >> common/networks.txt
echo '... StackStorm container IP retrieved'

# get DefectDojo container IP (for use by StackStorm)
dd_key="DD_IP="
dd_value=$(sudo docker network inspect banzai_default | grep -A 3 'banzai_dojo_1' | grep 'IPv4' | sed 's/.*: "//' | sed 's/\/.*//')
dd_ip=$dd_key$dd_value
echo $dd_ip >> common/networks.txt
echo '... DefectDojo container IP retrieved'

# generate + retrieve StackStorm api key
ss="SS_APIKEY="
ss_apikey=$(sudo docker exec stackstorm st2 apikey create -k)
echo $ss$ss_apikey >> common/api_keys.txt
echo '... StackStorm API Key retrieved'

# retrieve DefectDojo api key
echo
echo 'Insert your DefectDojo API Key:'
read dd_apikey
echo

dd="DD_APIKEY="
echo $dd$dd_apikey >> common/api_keys.txt
echo '... DefectDojo API Key retrived'

echo '============================================================'
echo '                       ADJUSTING SETTINGS                   '
echo '============================================================'

# adjusting DefectDojo "ALLOWED_HOSTS" settings
sudo docker exec banzai_dojo_1 sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\"\*\"\]/' /opt/django-DefectDojo/dojo/settings.py
echo '... Django "ALLOWED_HOSTS" settings adjusted'

echo '============================================================'
echo '                  INSTALLING CONTAINER PACKAGES             '
echo '============================================================'

# install pip - python package manager
sudo docker exec stackstorm bash -c 'echo 'Y' | sudo apt-get install python-pip'
echo '... pip successfully installed'
echo

# install DefectDojo Python module
sudo docker exec stackstorm bash -c 'echo 'Y' | sudo pip install -U defectdojo_api'
echo '... defectdojo_api module successfully installed'
echo

# upgrade Python Requests module
sudo docker exec stackstorm bash -c 'sudo pip install -U requests'
echo '... Python requests module successfully updated'
echo

# install nmap
sudo docker exec stackstorm bash -c 'echo 'Y' | sudo apt-get install nmap'
echo '... nmap successfully installed'
echo

echo '============================================================'
echo '                        SETUP COMPLETE                      '
echo '    execute "run_datafetch.bash" to complete the launch     '
echo '                                                            '
echo '      RUN "sudo docker-compose down" TO STOP SERVICES       '
echo '============================================================'

