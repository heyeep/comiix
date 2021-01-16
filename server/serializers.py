from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class meta:
        model = Author
        fields = ('first_name', 'last_name', 'email', 'message')
