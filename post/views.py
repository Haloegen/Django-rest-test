from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_API.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
  serializer_class= PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Post.objects.annotate(
    comments_count = Count('comment', distinct = True),
    likes_count = Count('likes', distinct = True)
  ).order_by('-created_at')
  filter_backends = [
    filters.OrderingFilter,
    filters.SearchFilter,
    DjangoFilterBackend,
  ]
  filterset_fields = [
    'owner__username__owner__profile',
    'likes__owner__profile',
    'owner__profile',
  ]
  search_fields = [
    'owner__username',
    'title',
  ]
  ordering_fields = [
    'comments_count', 
    'likes_count',
    'likes__created_at'
  ]
    


  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = PostSerializer
  queryset = Post.objects.annotate(
    comments_count = Count('comment', distinct = True),
    likes_count = Count('likes', distinct = True)
  ).order_by('-created_at')