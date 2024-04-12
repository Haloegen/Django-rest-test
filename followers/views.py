from rest_framework import generics, permissions
from drf_API.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

class LikeList(generics.ListCreateAPIView):
  serializer_class= FollowerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Follower.objects.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = FollowerSerializer
  queryset = Follower.objects.all()
