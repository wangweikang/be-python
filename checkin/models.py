from common.models import BaseModel
from django.db import models

class WxUser(BaseModel):
    nick_name = models.CharField(verbose_name='产品名称', max_length=200, null=True, blank=True)
    avatar_url = models.CharField(verbose_name='头像url', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '微信用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class Comments(BaseModel):
    user = models.ForeignKey(WxUser, on_delete=models.CASCADE)
    comments = models.CharField(verbose_name='留言', max_length=1000)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments
