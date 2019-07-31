from rest_framework.permissions import AllowAny
from checkin.models import WxUser, Comments
from rest_framework.viewsets import ModelViewSet
from .serializers import WxUserSerializer, CommentsSerializer


class CheckInViewSet(ModelViewSet):
    queryset = WxUser.objects.all()
    serializer_class = WxUserSerializer
    permission_classes = (AllowAny, )
    

class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny, )
