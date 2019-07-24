from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, boy. You are at the polls index.")
