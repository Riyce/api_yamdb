from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    TitleViewSet,
    #ReviewViewSet,
    #CommentViewSet,
    CategorieViewSet,
    GenreViewSet,
)


router = DefaultRouter()
router.register(
    r'titles',
    TitleViewSet,
)
#router.register(
    #r'titles/(?P<id>\d+)/reviews',
    #ReviewViewSet,
    #basename='reviews'
#)
#router.register(
    #r'titles/(?P<id>\d+)/reviews/(?P<id>\d+)/comments',
    #CommentViewSet,
    #basename='comments'
#)
router.register(
    r'categories/',
    CategorieViewSet,
)
router.register(
    r'genres/',
    GenreViewSet,
)

urlpatterns = [
    path('', include(router.urls)),
]
