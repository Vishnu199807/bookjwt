from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("books/list/", views.PublicView.as_view(), name="book_list"),
    path("books/create/", views.BookCreate.as_view(), name="create_book"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("register/", views.Register.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
]
