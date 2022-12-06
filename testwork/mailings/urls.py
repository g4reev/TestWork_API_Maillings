from django.urls import include, path
from rest_framework import routers

from .views import ClientViewSet, MailingViewSet, MessageLogViewSet

router = routers.DefaultRouter()
router.register('contacts', ClientViewSet)
router.register('mailings', MailingViewSet)
router.register('message_log', MessageLogViewSet)

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
