from rest_framework_mongoengine.serializers import DocumentSerializer

from api.models import User, Post


class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'
