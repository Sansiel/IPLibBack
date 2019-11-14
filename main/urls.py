from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('author', views.AuthorViewSet.as_view()),
    path('book', views.BookViewSet.as_view()),
    path('upload', views.FileUploadView.as_view()),
    path('ws/', views.BookView.as_view()),
]