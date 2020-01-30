# W251

# Project Overview

This project consists of an IoT application pipeline that has components running both in the Jetson TX2 as well as the cloud. This pipeline captures faces from a video stream in real time, and then it transmits these images to the cloud in real time. Some of these sample images that are uploaded to IBM cloud object storage are listed under the "Images in Bucket" directory.

The network of hw03 was created in the Jetson with the command:

```
docker network create --driver bridge hw03
```

This network was also created in the cloud with the same command.  

Each of the folders consists of both the Dockerfile used to build the container, as well as the shell script to execute the build and/or run the container. Moreover, the python files are included where applicable. The topic that is used is called facedetection, and the url for the object storage is here: https://w251-bucket-sayan.s3.us-south.cloud-object-storage.appdomain.cloud
