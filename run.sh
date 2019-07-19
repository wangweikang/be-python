#!/bin/bash
docker-compose build
docker-compose up -d
# docker-compose scale redis-slave=2
# docker-compose scale sentinel=3
# docker-compose scale web=3


# 启动swarm模式
docker swarm init
# 构建nginx network
docker network create nginx-net --attachable --scope swarm
# 独立创建volume
docker volume create nginx-conf
docker volume create nginx-vhost
docker volume create nginx-html
docker volume create nginx-dhparam
docker volume create nginx-certs
# 以 stack 的模式启动 nginx
docker stack deploy -c nginx.yml nginx
# 以 stack 的模式启动 portainer
docker stack deploy -c portainer.yml portainer
# 创建registry的volumes
docker volume create registry_data
docker volume create registry_auth
# 生成register密码
cd /var/lib/docker/volumes/registry_auth/_data
docker run --entrypoint htpasswd registry:2 -Bbn 用户名 密码 > .passwd
# 以 stack 的模式启动 register
docker stack deploy -c register.yml register
# 取消 nginx 默认最大传输大小限制
cd /var/lib/docker/volumes/nginx-vhost/_data
echo "client_max_body_size 0;" > registry.thiswjk.xyz
