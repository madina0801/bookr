from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="base"),
    path("books/", views.book_list, name="book_list"),
	path("search-result/", views.search),
	path('books/<int:pk>/', views.book_detail, name='book_detail')
]
