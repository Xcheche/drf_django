from rest_framework import serializers  # Importing the serializer
from .models import Movie  # Importing the Movie model


class MovieSerializer(serializers.ModelSerializer):  # Defining the serializer
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:  # Defining the meta class
        model = Movie  # Defining the model
        # fields = "__all__"  # Defining the fields
        fields = ["id", "name", "duration", "rating", "url", "type", "image"]
