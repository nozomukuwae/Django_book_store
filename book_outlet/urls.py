from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.book_detail, name='book-detail')
]
