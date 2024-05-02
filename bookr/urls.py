from django.contrib import admin
from django.urls import include, path
import reviews.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('reviews.urls')),
	path('book-search', reviews.views.search)
]
