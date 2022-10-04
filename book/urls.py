from .views import TypeList, BookList, TypeDetail, BookDetail
from django.urls import path

urlpatterns = [
    path('type/', TypeList.as_view()),
    path('type/<int:pk>/', TypeDetail.as_view()),

    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
]