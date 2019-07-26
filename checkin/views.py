from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from checkin.models import WxUser, Comments


class CheckInCreate(CreateView):
    model = WxUser
    fields = ['nick_name', 'avatar_url']


class CommentCreate(CreateView):
    model = Comments
    fields = ['user_nick_name', 'comments']


class CommentUpdate(UpdateView):
    model = Comments
    fields = ['user_nick_name', 'comments']

# class CommentDelete(DeleteView):
#     model = Comments
#     success_url = reverse_lazy('')