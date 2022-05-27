from django.urls import path, include
from rest_framework.routers import SimpleRouter
from room.views import RoomViewSet

router = SimpleRouter(trailing_slash=False)
router.register('rooms', RoomViewSet, basename='rooms')

urlpatterns = [
    path('', include(router.urls)),
]