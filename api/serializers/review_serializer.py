from rest_framework import serializers

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    
    
    # author = serializers.SlugRelatedField(
     #   read_only=True,
     #   slug_field="author"
    #)

    class Meta:
        exclude = ('id',)
        model = Review