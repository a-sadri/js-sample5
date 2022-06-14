from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, OrderItem

def hello(request):
    queryset = Product.objects.select_related('collection').all()
    
    return render(request, 'hello.html', {'query_set': queryset})
