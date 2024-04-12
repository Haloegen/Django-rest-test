from rest_framework import generics
from drf_API.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
  serializer_class= ProfileSerializer
  queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()
