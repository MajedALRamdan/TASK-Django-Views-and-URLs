from .models import Pokemon
from django.http import HttpRequest,HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import ListPokemonSerializer




def PokemonD(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(  f"""\
        <p>Name: {pokemon_db.name}</p>
        <p>Type: {pokemon_db.type}</p>
        <p>HP: {pokemon_db.hp}</p>""")   

def PokemonAll(request: HttpRequest) -> HttpResponse:
    pokemons = Pokemon.objects.all().values_list("name", flat=True)
    joined = "\n".join(f"<li>{name}</li>" for name in pokemons)
    return HttpResponse(f"<ul>{joined}</ul>")
    
class PokeListApiView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = ListPokemonSerializer