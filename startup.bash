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

# remove old env variables
> common/networks.txt
> common/api_keys.txt
echo '... Old env variables removed successfully'

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


# get Burp container IP (for use by StackStorm)
burp_key="BURP_IP="
burp_value=$(sudo docker network inspect banzai_default | grep -A 3 'burpdock' | grep 'IPv4' | sed 's/.*: "//' | sed 's/\/.*//')
burp_ip=$burp_key$burp_value
echo $burp_ip >> common/networks.txt
echo '... Burp container IP retrieved'

# generate + retrieve StackStorm api key
ss="SS_APIKEY="
ss_apikey=$(sudo docker exec stackstorm st2 apikey create -k)
echo $ss$ss_apikey >> common/api_keys.txt
echo '... StackStorm API Key retrieved'

# retrieve DefectDojo api key
echo
echo 'Insert your DefectDojo API Key to continue:'
echo
echo 'To find the key, log in to DefectDojo through your web browser and go to the "API Key" page.'
read dd_apikey
echo

dd="DD_APIKEY="
echo $dd$dd_apikey >> common/api_keys.txt
echo '... DefectDojo API Key retrieved'

echo '============================================================'
echo '                       ADJUSTING SETTINGS                   '
echo '============================================================'

# adjusting DefectDojo "ALLOWED_HOSTS" settings
sudo docker exec banzai_dojo_1 sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\"\*\"\]/' /opt/django-DefectDojo/dojo/settings.py
echo '... Django settings adjusted'

echo '============================================================'
echo '                 INSTALLING ADDITIONAL PACKAGES             '
echo '============================================================'

echo '... INSTALLING STACKSTORM COMPONENTS'

sudo docker exec stackstorm bash -c 'sudo apt-get install -y python-pip'                # python pip
sudo docker exec stackstorm bash -c 'echo 'Y' | sudo pip install -U defectdojo_api'     # defectdojo
sudo docker exec stackstorm bash -c 'sudo pip install -U requests'                      # requests
sudo docker exec stackstorm bash -c 'sudo apt-get install -y nmap'                      # nmap

echo '============================================================'
echo '                        SETUP COMPLETE                      '
echo '                                                            '
echo '      RUN "sudo docker-compose down" TO STOP SERVICES       '
echo '============================================================'

echo '============================================================'
echo '                    RUNNING DATAFETCH SERVER                '
echo '                                                            '
echo '         This needs to run for the life of the pipeline     '
echo '============================================================'

# run datafetch script
sudo docker exec -it banzai_dojo_1 bash -c 'python findme/insertnmap.py'
sudo docker exec -it banzai_dojo_1 bash -c 'python findme/datafetch.py'
