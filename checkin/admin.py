from django.contrib import admin
from checkin.models import WxUser, Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'comments')


admin.site.register(WxUser)
admin.site.register(Comments, CommentsAdmin)