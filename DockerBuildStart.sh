# stop all containers
docker stop $(docker ps -q)
# delete all containers
docker rm $(docker ps -q -a)

docker image rm $(docker images -q)
docker image build -t mysql-1:latest . 
docker run --name mysql-1  -d -p 3306:3306 mysql-1:latest
export CONTAINERID=$(docker ps -q | head -1)
docker exec -it $CONTAINERID bash