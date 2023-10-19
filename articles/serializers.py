from rest_framework import serializers
from .models import Article, Tag, Category, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        return None


    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username

    def get_article(self, obj):
        return obj.article.title
