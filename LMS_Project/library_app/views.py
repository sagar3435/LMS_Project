from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Admin, Book
from .serializers import AdminSerializer, LoginSerializer, BookSerializer
from .permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class AdminSignupView(APIView):
    """
    API endpoint for admin signup.
    Allows creation of a new admin account.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    """
    API endpoint for admin login.
    Returns access and refresh tokens on valid credentials.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.validated_data['admin']
            refresh = RefreshToken.for_user(admin)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookCreateView(APIView):
    """
    API endpoint to create a new book.
    Admin authentication required.
    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListView(APIView):
    """
    API endpoint to list all books.
    Accessible by both admin and students (public view) not required authentication.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookUpdateView(APIView):
    """
    API endpoint to update book details.
    Admin authentication required.
    """
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    """
    API endpoint to delete a book.
    Admin authentication required.
    """
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({"message": "Book deleted"}, status=status.HTTP_204_NO_CONTENT)
