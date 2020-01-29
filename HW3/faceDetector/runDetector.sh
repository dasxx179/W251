docker build -t detector -f Dockerfile.faceDetector .
docker run --name detector --network hw03 -e DISPLAY=$DISPLAY --privileged -v /tmp:/tmp --rm -ti detector
