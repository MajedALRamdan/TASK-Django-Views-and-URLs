from rest_framework import serializers
from .models import Pokemon

class ListPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'