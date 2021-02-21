from rest_framework import serializers

from .models import Category, Genre, Review, Title


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
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate(self, data):
        #if Review.objects.filter(
        #    title=self.context['view'].kwargs.get('title_id'),
        #    author=self.context['request'].user
        #).exists:
        #    raise serializers.ValidationError(
        #        'You have written review to this title.'
        #    )
        score = data['score']
        if score <= 0 or score > 10:
            raise serializers.ValidationError(
                'Reiting must be from 1 to 10'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Review
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['title', 'author']
            )
        ]        
