from django.urls import include, path
from rest_framework import routers

from ratings.views import RatingViewSet 

router = routers.DefaultRouter()
router.register(r"ratings", RatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("ratings/new/<int:trip_id>/<int:driver_id>", RatingViewSet.as_view({"post": "create"}))
]