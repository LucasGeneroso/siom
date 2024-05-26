from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from apps.occurrence.models import Occurrence
from apps.occurrence.api.serializers import OccurrenceSerializer



# /occurences > route url > viewset > get data in model > return with serializer
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, JWTAuthentication])
class OccurenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    search_fields = ['neighborhood']
    filterset_fields = ['neighborhood', 'city', 'state', 'type', 'date']
    ordering_fields = ['id', 'neighborhood']


@method_decorator(login_required, name='dispatch')
class ProtectedTemplateView(TemplateView):
    pass
