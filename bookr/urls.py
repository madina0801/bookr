from django.contrib import admin
from django.urls import path
import reviews.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', reviews.views.index),
	path('book-search', reviews.views.search)
]
