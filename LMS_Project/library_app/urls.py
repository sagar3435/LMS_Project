from django.urls import path
from .views import (
    AdminSignupView, AdminLoginView,
    BookCreateView, BookListView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
