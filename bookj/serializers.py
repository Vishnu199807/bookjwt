from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","firstname","lastname", "email", "password"]

    def save(self):
        register = User(
            username=self.validated_data["username"],
            firstname= self.validated_data["firstname"],
            lastname= self.validated_data["lastname"],
            email=self.validated_data["email"],

        )
        password = self.validated_data["password"]
        register.set_password(password)
        register.save()
        return register


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    title = serializers.CharField(
        min_length=4,
        max_length=100,
        validators=[UniqueValidator(queryset=Book.objects.all())],
    )

    class Meta:
        model = Book
        fields = ["id", "title", "description", "author", "price", "user"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero, Enter a valid price")
        return value