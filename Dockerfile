FROM django:latest

COPY ./app /www/be-python/app

COPY supervisord.conf /etc/supervisord.conf

COPY gunicorn_conf.py /etc/gunicorn_conf.py

RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

RUN pip install meinheld && \
    pip install gunicorn && \
    cd /www/be-python/app && \
    pip install -r requirement.txt && \
    python manage.py makemigrations && \
    python manage.py migrate

WORKDIR /www/be-python/app

CMD supervisord -c /etc/supervisord.conf
