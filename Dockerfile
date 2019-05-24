FROM django:latest

COPY ./app /usr/src/app

COPY supervisord.conf /etc/supervisord.conf

COPY gunicorn_conf.py /etc/gunicorn_conf.py

RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

RUN pip install meinheld && \
    pip install gunicorn && \
    cd /usr/src/app && \
    pip install -r requirement.txt && \
    python manage.py makemigrations && \
    python manage.py migrate

WORKDIR /usr/src/app

CMD supervisord -c /etc/supervisord.conf
