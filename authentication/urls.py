from dj_rest_auth.registration.views import RegisterView
from django.conf.urls import include
from django.urls import path, re_path

from authentication.serializers import CustomRegisterSerializer

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    # Custom serializer for registration
    path(
        "registration/",
        RegisterView.as_view(serializer_class=CustomRegisterSerializer),
        name="custom_register",
    ),
    # Use default endpoints for resend-email and verify-email
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("account/", include("allauth.urls")),
]
