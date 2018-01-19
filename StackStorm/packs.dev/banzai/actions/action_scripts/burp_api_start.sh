#!/bin/bash

# start Burp API service

echo 'Starting Burp API service'
java -jar opt/burp/burp-rest-api/build/libs/burp-rest-api-1.0.0.jar
