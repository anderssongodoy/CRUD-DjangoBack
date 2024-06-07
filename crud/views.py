from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    data = {"books": list(books.values("id", "title", "author"))}
    return JsonResponse(data)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = {"id": book.id, "title": book.title, "author": book.author}
    return JsonResponse(data)

@csrf_exempt
def book_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book = Book.objects.create(title=data["title"], author=data["author"])
        return JsonResponse({"id": book.id, "title": book.title, "author": book.author})
    return HttpResponse(status=405)

from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookList(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)