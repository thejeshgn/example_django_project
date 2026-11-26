from rest_framework import viewsets

from .models import Case
from .serializers import CaseSerializer
from .tasks import hello_message


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.prefetch_related("parties__person")
    serializer_class = CaseSerializer

    def perform_create(self, serializer):
        serializer.save()
        print("before calling hello_message")
        hello_message.send()
        print("after calling hello_message")
