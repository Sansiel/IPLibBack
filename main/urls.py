from django.urls import path

from . import views

urlpatterns = [
    path('author', views.AuthorViewSet.as_view()),
    path('book', views.BookViewSet.as_view()),
]