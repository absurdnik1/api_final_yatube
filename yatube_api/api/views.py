from rest_framework import permissions, viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


from .permissions import OwnerOrReadOnly
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer,
    FollowSerializer)
from posts.models import Post, Group


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Post.objects.select_related('group', 'author')

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def get_queryset(self):
        return self.request.user.follower


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        return serializer.save(author=self.request.user, post=post)
