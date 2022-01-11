# NGINX Log Parser/Auditor

Python script processes nginx.log file to check ingress activity/frequency. 
Also checks for how many unique inbound ips belong to specific subnets. 

## Dependencies
- python3.10 `brew install python3.10`
- regex `pip3 install regex`
- ipaddress `pip3 install ipaddress`
- copy (built in)

## Getting Started
- clone repo to local `https://github.com/hannerific/nginx-log-parser`
- `python3 carta.py` from repo in local machine
- `docker build -t nginx:carta-image`
- `docker run -it -d --publish 8080:80 -v log_audit.html:/var/log/html --name carta-container nginx:carta-image`
- navigate to `localhost:8080` in browser

## Improvements/To Dos
- convert python script to executable file that runs on build
- edit Dockerfile to install dependencies for executable python script
```
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python3.10 python3-pip git
RUN pip3 install regex ipaddress
COPY carta.py /carta.py
COPY nginx.log /nginx.log
```    
- refactor to handle either single or multiple *.log files
- find python templating package instead of using f.write to write raw html
- abstract log parser by wrapping into class to process log files for different info, not just ip frequency (chef could be interesting to implement this)
- build out into microservice that processes various logs 
- backup log audit results to cloud server with appropriate bucket policy for various audits i.e. SOX

## Reminders
- check local `/etc/hosts` file config if experiencing issues with localhost:8080 
