#!/bin/bash

# url param specified in nmap_chain
url=$1

sudo nmap $url -oX /opt/stackstorm/scan_output/nmap_results.xml
