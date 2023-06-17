from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

import posts.models as ps

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = ps.Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
        model = ps.Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ps.Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate(self, data):
        if self.context.get("request").user == data['following']:
            raise serializers.ValidationError(
                'Подписка на самого себя невозможна')
        return data

    class Meta:
        model = ps.Follow
        fields = ('user', 'following')
        validators = (
            UniqueTogetherValidator(
                queryset=ps.Follow.objects.all(),
                fields=('user', 'following'),
                message='Подписка уже оформлена'
            ),
        )
