# W251

# Project Overview

This project consists of an IoT application pipeline that has components running both in the Jetson TX2 as well as the cloud. This pipeline captures faces from a video stream in real time, and then it transmits these images to the cloud in real time. Some of these sample images that are uploaded to IBM cloud object storage are listed under the "Images in Bucket" directory.

# Jetson Overview

The network that was used by the containers running in the Jetson was created with the following command:

```bash
docker network create --driver bridge hw03
```

There are three main components to the Jetson:

* Face Detector
* Broker
* Forwarder

Each of the folders contain the bash script used to build the docker containers as well as the Dockerfiles that provide the instructions for the container.  Moreover, the forwarder and face detector folders contain the python code that was used to capture pictures from the camera.  This was accomplished with OpenCV, and these images were subsequently passed on to the Mosquitto broker.  The messages were in byte form for the transfers.  After this, the broker sent the message to the forwarder which sent the image to the remote instance running in the cloud for processing.  

# Instance Overview

There are two main components to the instance:

* Broker/Receiver
* Processor

A network is setup with the following command:

```bash
docker network create --driver bridge hw03
```

The receiver is a mosquitto broker that gets the messages that the forwarder from the previous section sent.  The processor is subscribed to this broker and captures these messages.  After the processor receives the messages, it transforms it to an image and saves it to an storage bucket in IBM Cloud.

# Final Results

The aforementioned storage bucket hosted in the IBM cloud is here: [https://w251-bucket-sayan.s3.us-south.cloud-object-storage.appdomain.cloud](https://w251-bucket-sayan.s3.us-south.cloud-object-storage.appdomain.cloud/)

The images are also under the "Images in Bucket" folder provided in the repo.  

# Problems

It was quite interesting setting up each of the components in the pipeline.  It was a bit difficult to understand the entire process all at once, so my mindset was to approach each task component by component.  I first focused on the Jetson, and subsequently, I worked on the two components in the cloud.  Debugging was also quite tedious, for there many moving parts to this pipeline.  Overall, it was a great project, and I apologize for the poor camera resolution!

