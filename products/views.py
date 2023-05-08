from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
import requests

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def index(request, id):
    return HttpResponse(f'The ID is: {id}')


url = f"http://localhost:8000/products/hogehoge/"

def index_get(request, id):
    response = requests.get(url + str(id) + "/")
    text = response.text
    return HttpResponse(text)

def index_get_all(request):
    response = requests.get(url)
    text = response.text
    return HttpResponse(text)

def index_post(request, name, price):
    data = {"name": name, "price": price}
    response = requests.post(url, data=data)
    return HttpResponse(response.text)

def index_patch(request, id, name, price):
    data = {"name": name, "price": price}
    response = requests.patch(url + str(id) + "/", data=data)
    return HttpResponse(response.text)

def index_delete(request, id):
    response = requests.delete(url + str(id) + "/")
    return HttpResponse(response.text)