# Abstract:

A simple tool to query the https://macaddress.io/ MAC address lookup API and get the company name associated with it. This tool is platform independent since it is containerized in an docker container.

# Usage and Requirements:
1. Docker installed
* Following dockerfile will create an Alpine Container with the tool in it.
* To use the tool we go into the docker container and run the main.py file as per the [Installation](#installation) procedure.


# Installation:

1. Navegate to the directory where the docker file is present
```
gaurav@gaurav-VirtualBox:~/Desktop/MMapsC$ pwd
/home/gaurav/Desktop/MMapsC
gaurav@gaurav-VirtualBox:~/Desktop/MMapsC$ ll
total 20
drwxrwxr-x 4 gaurav gaurav 4096 Oct 15 14:47 ./
drwxr-xr-x 5 gaurav gaurav 4096 Oct 15 14:02 ../
drwxrwxr-x 2 gaurav gaurav 4096 Oct 15 14:47 app/
-rw-rw-r-- 1 gaurav gaurav  116 Oct 15 15:00 Dockerfile
drwxrwxr-x 8 gaurav gaurav 4096 Oct 15 15:26 .git/
gaurav@gaurav-VirtualBox:~/Desktop/MMapsC$
```

2.  Run the following command to build an image out of it
* Here, named 'mmapc'
```
docker build -t mmapc .
```

# Usage:

1. Run the tool
```
docker run --dns 8.8.8.8 mmapc [-mac MAC] [-apikey APIKEY]
```
example: 
```
docker run --dns 8.8.8.8 mmapc -mac 44.38.39.ff.ef.57 -apikey at_olrz0Ny9kHhc3oYVzQ7b7Z74NkwfD
```

Or execute help argument
```
/app # docker run mmapc -h
usage: main.py [-h] [-mac MAC] [-apikey APIKEY]

Take MAC Address as input, API Key as well if required

optional arguments:
  -h, --help            show this help message and exit
  -mac MAC, --macaddress MAC
                        Please provide a valid MAC address
  -apikey APIKEY, --apikey APIKEY
                        Please provide a valid API Key
/app # 
```
# Security Measures:
- Validation for a valid mac address is also taken care of in the code itselft.
- The container is not exposing any ports since we don't have GUI for this tool.

# Support:
- gsukhatm@cisco.com
- https://macaddress.io/api

**Free Software!**
