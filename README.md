## Overview

The aim of the AppSec pipeline is to provide the ability to perform automated security assessments against a system. The pipeline should help reduce the amount of time spent on repetitive AppSec activities, to optimise use of a security team. It should also be a tool that can serve as a consistent process which can be followed by security teams.

## Setup

1. Setup the pipeline by running: <pre>$ ./startup.bash</pre>
This will also start a webhook service between DefectDojo and StackStorm. This process must be kept running throughout the life of the pipeline.

2. Download a Burp Suite Professional .jar file and place it in the `/burp-rest-api/lib` directory.

3. Access the `Burpdock` container by running: <pre>$ sudo docker exec -it burpdock bash</pre>

4. Inside the container, navigate to `opt/burpdock/burp-rest-api` and build the Burp Suite .jar by running: <pre>$ gradle clean build</pre>
An error message may show up during the build, but this is irrelevant and can be ignored.

5. Once Burp is built, launch the API service: <pre>$ java -jar build/libs/burp-rest-api-1.0.0.jar</pre>
You will be prompted to enter your Burp Professional license. Keep this process running throughout the life of the pipeline.

## Access services

StackStorm
* Container: <pre>$ sudo docker exec -it stackstorm bash</pre>
* UI: `localhost`

DefectDojo
* Container: <pre>$ sudo docker exec -it banzai_dojo_1 bash</pre>
* UI: `localhost:8000`

Burp Rest API
* Container: <pre>$ sudo docker exec -it burpdock bash</pre>

Google Gruyere
* Container: <pre>$ sudo docker exec -it gruyere bash</pre>
* UI: `localhost:8008`

## Help

For more detailed information, go to the repository's Wiki page: https://github.com/brianlam38/Banzai/wiki.

## Contributors

* Brian Lam
* Jacqueline Lee
