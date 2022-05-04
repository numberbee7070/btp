import os
import random
from base64 import b64decode, b64encode

import numpy as np
from deepface import DeepFace
from deepface.commons import distance
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from django.http.response import HttpResponse
from rest_framework.views import APIView

from .models import Student
from .serializers import UserSerializer, StudentSerializer
import json


def get_photo_embeddings(path):
    return np.array(
        DeepFace.represent(path, model_name="Facenet", detector_backend="mtcnn"),
        dtype="float32",
    )


class SignupView(CreateAPIView):
    serializer_class = UserSerializer


class CreateStudentView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        obj = serializer.instance
        obj.photo_embeddings = b64encode(get_photo_embeddings(obj.photo.path).tobytes())
        obj.save()


def create_temp_file(name, f):
    with open(name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def face_authentication_view(request):
    if request.method == "POST":
        img = request.FILES["image"]
        var = random.randint(1, 10000)
        os.makedirs("/tmp/swasthshala", exist_ok=True)
        filename = f"/tmp/swasthshala/{var}_{img.name}"
        create_temp_file(filename, img)

        try:
            uploaded_embeds = get_photo_embeddings(filename)
            highest_match = (1, None)
            for st in Student.objects.all():
                st_embeds = np.frombuffer(
                    b64decode(st.photo_embeddings),
                    dtype="float32",
                )
                dst = distance.findCosineDistance(st_embeds, uploaded_embeds)
                if highest_match[0] > dst:
                    highest_match = (dst, st)
            return HttpResponse(
                json.dumps(StudentSerializer(instance=highest_match[1]).data)
            )

        except Exception as e:
            print(e)
            return HttpResponse(
                "can not process image",
                status=status.HTTP_400_BAD_REQUEST,
            )

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
