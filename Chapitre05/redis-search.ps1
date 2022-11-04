# On lance un serveur RediSeach dans Docker
docker pull redislabs/redisearch
docker run -d -p 6379:6379 --name redisearch redislabs/redisearch

pip install redisearch

docker exec -it redisearch /bin/bash