from .views import TypeList, ShelfList, TypeDetail, ShelfDetail
from django.urls import path

urlpatterns = [
    path('type/', TypeList.as_view()),
    path('type/<int:pk>/', TypeDetail.as_view()),

    path('book/', ShelfList.as_view()),
    path('book/<int:pk>/', ShelfDetail.as_view()),
]
