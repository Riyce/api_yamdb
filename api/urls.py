from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,  ReviewViewSet, CommentViewSet,
                    GenreViewSet, TitleViewSet)

router = DefaultRouter()
router.register(
    r'titles',
    TitleViewSet,
)
router.register(
    r'titles/(?P<id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<id1>\d+)/reviews/(?P<id2>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'categories',
    CategoryViewSet,
)
router.register(
    r'genres',
    GenreViewSet,
)

urlpatterns = [
    path('', include(router.urls)),
]