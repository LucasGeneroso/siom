from django.urls import path, include
from rest_framework import routers

from apps.occurrence.api.views import OccurenceViewSet, ProtectedTemplateView


router = routers.DefaultRouter()
router.register("occurrences", OccurenceViewSet)

api_router = [
    path("", include(router.urls)),
    path("occurrences-page/", 
         ProtectedTemplateView.as_view(template_name="occurrences.html"), 
         name='occurrences-page'),
]
