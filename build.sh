#!/bin/bash

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
docker-compose -f docker-compose.yml scale redis-slave=2
docker-compose -f docker-compose.yml scale sentinel=3
docker-compose -f docker-compose.yml scale ping-app=3

APP_SERVERS=$(docker-compose -f docker-compose.yml ps ping-app | awk '{print $1}' |sed '1,2d'|xargs docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' | xargs)
APP_SERVER_PORT=8000
INDEX=1
for ETCD_NODE in ${APP_SERVERS//\s/};
do
    docker-compose -f docker-compose.yml exec etcd etcdctl set /app/servers/app$INDEX $ETCD_NODE:$APP_SERVER_PORT
    INDEX=$(expr $INDEX + 1)
done
