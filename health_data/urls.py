from django.urls import path
from .views import CreateHealthRecordView

urlpatterns = [
    path("create/", CreateHealthRecordView.as_view()),
]
