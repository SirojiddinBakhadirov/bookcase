from .models import Type, Book
from rest_framework import serializers


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
