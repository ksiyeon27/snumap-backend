from django.urls import path, include
from rest_framework.routers import SimpleRouter
from place.views import PlaceViewSet

# place_detail = PlaceDetailView.as_view({'get':'get'})
# urlpatterns = [
#     path('place/<int:id>', place_detail)
# ]

router = SimpleRouter(trailing_slash=False)
router.register('places', PlaceViewSet, basename='places')

urlpatterns = [
    path('', include(router.urls)),
]