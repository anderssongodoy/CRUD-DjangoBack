from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary']

    def get_summary(self, obj):
        return f"{obj.title} by {obj.author}"