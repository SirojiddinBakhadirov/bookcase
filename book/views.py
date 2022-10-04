from django.shortcuts import render
from .models import Type, Shelf
from .serializers import TypeSerializers, BookSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TypeList(ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class TypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class ShelfList(ListCreateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = BookSerializers


class ShelfDetail(RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = BookSerializers




