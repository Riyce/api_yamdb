from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    TitleViewSet,
    ReviewViewSet,
    #CommentViewSet,
    CategoryViewSet,
    GenreViewSet,
)


router = DefaultRouter()
router.register(
    r'titles',
    TitleViewSet,
    basename='Titles'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Reviews'
)
#router.register(
#    r'titles/(?P<id>\d+)/reviews/(?P<id>\d+)/comments',
#    CommentViewSet,
#    #basename='comments'
#)
router.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)
router.register(
    r'genres',
    GenreViewSet,
    basename='Genres'
)

urlpatterns = [
    path('', include(router.urls)),
]