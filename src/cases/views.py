from rest_framework import viewsets

from .models import Case
from .serializers import CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.prefetch_related("parties__person")
    serializer_class = CaseSerializer
