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