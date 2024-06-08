"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import book_list, book_detail, book_create, BookListView, BookListAPIView, BookDetailView, BookDetailAPIView, PublisherListCreateView, PublisherRetrieveUpdateDestroyView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/create/', book_create, name='book_create'),

    path('apiview/books/', BookListView.as_view(), name='apiview-book-list'),
    path('apiview/books/<int:pk>/', BookDetailView.as_view(), name='apiview-book-detail'),

    path('apiview2/books/', BookListAPIView.as_view(), name='book-list'),
    path('apiview2/books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    path('publishers/', PublisherListCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateDestroyView.as_view(), name='publisher-detail'),

    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
]

# from rest_framework.routers import DefaultRouter
# from crud.views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = router.urls