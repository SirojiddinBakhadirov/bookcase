from django.shortcuts import render
from .models import Type, Book
from .serializers import TypeSerializers, BookSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TypeList(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class TypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers




