from rest_framework import serializers  # Importing the serializer
from .models import Movie  # Importing the Movie model


class Movie(serializers.ModelSerializer):  # Defining the serializer
    class Meta:  # Defining the meta class
        model = Movie  # Defining the model
        fields = "__all__"  # Defining the fields
