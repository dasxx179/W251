docker build -t mosquitto -f Dockerfile.localbroker .
docker run --name mosquitto --network hw03 -p 1883:1883 --rm -ti mosquitto
