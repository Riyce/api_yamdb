from rest_framework import serializers

from .models import Category, Genre, Title, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class TitleCreateUpdateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre', 'category', 'description', )


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre', 'category', 'description', )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        #exclude = ('id',)
        fields = '__all__'
        model = Review       


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        #exclude = ('id',)
        fields = '__all__'
        model = Review  