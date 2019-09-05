from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from api.models import User, Post
from api.serializers import UserSerializer, PostSerializer


class UserViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class PostViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
