from django.shortcuts import render
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
#from rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly)
from ..models import Review

#from .permissions import IsOwnerOrReadOnly
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

def get_queryset(self):
        #rev = get_object_or_404(Review, id=self.kwargs['review_id'])
        return Review.objects.filter(author=request.user, title=data['title']).exists

    #def perform_create(self, serializer):
        #serializer.save(author=self.request.user)