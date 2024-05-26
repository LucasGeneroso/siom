from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.occurrence.api.urls import api_router
from apps.authorization.urls import router
from apps.authorization.views import register, login_view, logout_view


urlpatterns = [
    path("siom/", include(router)),
    path("siom/api/", include(api_router)),
    path("siom/api/register/", register, name="register"),
    path("siom/api/login/", login_view, name="login"),
    path("siom/api/logout/", logout_view, name="logout"),
    path("siom/api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # authentification
    path("siom/api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # authentification
    path("siom/api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # authentification
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
