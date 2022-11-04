docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis01
docker run --name redis02 -d redis redis-server --slaveof 172.17.0.2 6379

docker logs redis02

docker exec -it redis02 /bin/bash

docker stop redis02 
docker rm redis02 
