from django.urls import path
from .Login import LoginAPIView
from .Register import RegisterAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
]
