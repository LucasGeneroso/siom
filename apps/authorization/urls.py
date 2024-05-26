from django.urls import path
from django.views.generic import TemplateView


router = [
    path("login-page/", TemplateView.as_view(template_name="login.html"), name="login-page"),
]
