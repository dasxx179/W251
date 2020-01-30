docker build -t localbroker -f Dockerfile.localbroker .
docker run --name localbroker --network hw03 -p 1883:1883 --rm -ti localbroker
