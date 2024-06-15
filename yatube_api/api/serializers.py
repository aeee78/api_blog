from django.contrib.auth import get_user_model
from rest_framework.relations import SlugRelatedField
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment

    def get_post(self, obj):
        return obj.post.id


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
