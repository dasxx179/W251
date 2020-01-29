docker build -t processor -f Dockerfile.processor .
docker run --name processor -v
/mnt/w251sayan/firstDirectory/HW03/:/mnt/w251sayan/firstDirectory/HW03 --network hw03 --rm -ti processor
