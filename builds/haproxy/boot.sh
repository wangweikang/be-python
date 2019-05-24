#!/bin/bash

./watcher.sh &

exec /docker-entrypoint.sh haproxy -f /usr/local/etc/haproxy/haproxy.cfg
