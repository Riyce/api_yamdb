from rest_framework.filters import SearchFilter
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin,UpdateModelMixin)
from rest_framework.pagination import PageNumberPagination
#from rest_framework.permissions import IsAuthenticatedOrReadOnly, 
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Category, Genre, Title, Review, Comments
from rest_framework import generics
#from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleCreateUpdateSerializer, TitleListSerializer,ReviewSerializer, CommentSerializer)


class ListCreateDestroyViewSet(CreateModelMixin,
                               DestroyModelMixin,
                               ListModelMixin,
                               GenericViewSet,
                               UpdateModelMixin #add
                               
                               ):
    pass


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    search_fields = ['name']
    filter_backends = [SearchFilter]
    lookup_field = 'slug'


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    search_fields = ['name']
    filter_backends = [SearchFilter]
    lookup_field = 'slug'


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleListSerializer
        return TitleCreateUpdateSerializer


class ReviewViewSet(ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    
#def get_queryset(self):
        #rev = get_object_or_404(Review, id=self.kwargs['review_id'])
 #       return Review.objects.filter(author=request.user, title=data['title']).exists

    #def perform_create(self, serializer):
        #serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination