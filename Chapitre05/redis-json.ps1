docker run -p 6379:6379 -d --name redisjson redislabs/rejson
docker exec -it redisjson redis-cli

docker stop redisjson
docker rm redisjson