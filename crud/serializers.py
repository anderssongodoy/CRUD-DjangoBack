from rest_framework import serializers
from .models import Book, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'publisher']

    def get_summary(self, obj):
        return f"{obj.title} by {obj.author}"