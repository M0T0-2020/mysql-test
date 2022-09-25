#!/bin/bash

docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql

# check process
docker ps

# connect container
# docker exec -it 'CONTAINER ID' bash