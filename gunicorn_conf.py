import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'meinheld.gmeinheld.MeinheldWorker'
user = 'root'
loglevel = 'warning'
reload = True
accesslog = '-'
# errorlog = '/var/log/gunicorn_error.log'
