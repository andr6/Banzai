#!/bin/bash

url=$1

sudo nmap $url -oX /opt/stackstorm/scan_output/nmap_results.xml
