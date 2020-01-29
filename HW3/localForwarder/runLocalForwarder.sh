docker run --rm --name localforwarder --network hw03 -v /tmp:/tmp -v $(pwd)/python:/localforwarder -ti localforwarder /bin/ash

