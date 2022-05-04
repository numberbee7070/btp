from rest_framework.generics import CreateAPIView
from .serializers import HealthRecordSerializer
from rest_framework.permissions import IsAuthenticated


class CreateHealthRecordView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HealthRecordSerializer
