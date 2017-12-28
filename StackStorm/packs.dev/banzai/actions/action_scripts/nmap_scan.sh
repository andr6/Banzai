#!/bin/bash

# STANDARD NMAP SCAN

# url param specified in nmap_chain
url=$1

sudo touch /opt/stackstorm/scan_results/nmap/nmap_standard.xml
sudo chmod +x /opt/stackstorm/scan_results/nmap/nmap_standard.xml
sudo nmap $url -oX /opt/stackstorm/scan_results/nmap/nmap_standard.xml
