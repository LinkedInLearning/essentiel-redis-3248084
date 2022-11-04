docker pull redislabs/redisgraph

docker run -p 6379:6379 -d --name redisgraph redislabs/redisgraph
docker exec -it redisgraph redis-cli