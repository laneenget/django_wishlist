import requests
from .models import CatFact

def get_cat_fact(request):
    response = requests.get('https://catfact.ninja/fact').json()
    fact = response['fact']
    CatFact(fact=fact).save()
    return HttpResponse('ok')