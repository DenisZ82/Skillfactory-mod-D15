from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user', 'rating']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'category_post', 'category_post_many', 'title', 'text', 'rating']


class PostCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['id', 'connectCategory', 'connectPost']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'rating']
