from .models import Book
from .serializers import UserRegisterSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound


class PublicView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Register(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "registered"
            data["email"] = account.email
            return Response({"message":"User registered Successfully"})
        else:
            data = serializer.errors
        return Response(data)


class BookCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Book deleted."})
        except NotFound:
            return Response({"message": "Book not found."})
