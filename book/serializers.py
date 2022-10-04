from .models import Type, Shelf
from rest_framework import serializers


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = "__all__"
