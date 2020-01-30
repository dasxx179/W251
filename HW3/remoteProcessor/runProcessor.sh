docker build -t processor -f Dockerfile.processor .
docker run --name processor -v
/mnt/w251-bucket-sayan/:/mnt/w251-bucket-sayan --network hw03 --rm -ti processor
