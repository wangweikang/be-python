from django.urls import path

from checkin.views import CheckInCreate, CommentCreate, AuthorUpdate

urlpatterns = [
    # path('', views.index, name='index'),
    path('/', CheckInCreate.as_view(), name='checkin'),
    path('/comments', CommentCreate.as_view(), name='comments'),
    path('/comments/<int:pk>/', AuthorUpdate.as_view(), name='update'),
]