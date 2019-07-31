from rest_framework import serializers
from common.serializers import BaseSerializer

from checkin.models import WxUser, Comments


class WxUserSerializer(BaseSerializer):

    class Meta:
        model = WxUser
        fields = '__all__'


class CommentsSerializer(BaseSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
