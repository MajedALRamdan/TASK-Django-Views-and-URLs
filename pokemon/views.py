from .models import Pokemon
from django.http import HttpResponse


def PokemonD(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(f"<ul>{pokemon}</ul>")   

def PokemonAll(request):
    pokemon = Pokemon.objects.all()
    pl="\n".join(f"<li>{pokemon}</li>" for pokemon in Pokemon.objects.all())
    return HttpResponse(f"<ul>{pl}</ul>")
    
    