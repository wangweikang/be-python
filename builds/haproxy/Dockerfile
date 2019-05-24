FROM haproxy:latest

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

COPY confd .

RUN chmod +x confd

COPY haproxy.toml /etc/confd/conf.d/

COPY haproxy.tmpl /etc/confd/templates/

COPY boot.sh .

COPY watcher.sh .

CMD ["./boot.sh"]
