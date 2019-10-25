# from django.urls import path

# from . import views

# urlpatterns = [
#     path('author', views.AuthorViewSet.as_view()),
#     path('book', views.BookViewSet.as_view()),
# ]

from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'author', views.AuthorViewSet, basename='author')
router.register(r'book', views.BookViewSet, basename='book')

urlpatterns = router.urls