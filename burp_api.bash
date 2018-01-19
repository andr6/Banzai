#!/bin/bash
echo '============================================================'
echo '                      BURP REST API SETUP                   '
echo '============================================================'

# remove old variables

# future enhancement:
# if burp_license exists, then skip setup and continue with launch
> common/burp_license.txt

echo "Please insert your Burp Professional license"
read burp_license
echo

echo $burp_license >> common/burp_license.txt
echo '... Retrieving Burp license'
echo

echo '============================================================'
echo '                LAUNCHING BURP REST API SERVICE             '
echo '============================================================'

sudo docker exec burpdock bash -c 'echo 'y' \ echo $burp_license \ java -jar opt/burpdock/burp-rest-api/build/libs/burp-rest-api-1.0.0.jar'
