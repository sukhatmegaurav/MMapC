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

3. Create a container out of it in deamon mode
* Here, container name is 'gvscontainer'
```
docker run -d --rm --name gvscontainer mmapc
```

# Usage:

1. Get into the alpine container
```
docker exec -it gvscontainer /bin/ash
```

2. Run the main.py file
```
python main.py [-mac MAC] [-apikey APIKEY]
```
example: 
```
python main.py -mac 44.38.39.ff.ef.57 -apikey at_0lsz0Ny9kHFc3oYVzQ7b7Z74NkwxB
```

Or execute help argument
```
/app # python main.py -h
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

# Support:
- gsukhatm@cisco.com
- https://macaddress.io/api

**Free Software!**
