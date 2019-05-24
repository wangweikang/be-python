from django.shortcuts import render
from django.http import HttpResponse

import redis
from redis.sentinel import Sentinel

sentinel = Sentinel([('sentinel', 26379)], socket_timeout=0.1)
rds = sentinel.master_for('master', socket_timeout=0.1)

# Create your views here.
def ping(request):
    rds.incr('count', 1)
    cnt = rds.get('count')
    cnt = b'0' if cnt is None else cnt
    return HttpResponse(cnt.decode())
