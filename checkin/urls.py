from django.urls import path
from rest_framework import routers

from checkin.views import CheckInViewSet, CommentViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('', CheckInViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
]
urlpatterns += router.urls