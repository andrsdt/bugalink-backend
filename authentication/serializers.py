from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import User


# https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#register-serializer
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = get_user_model()()
        self.cleaned_data = self.get_cleaned_data()
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        # Add more custom fields here as needed
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        print("A".center(80, "-"))
        print(user)
        return user
