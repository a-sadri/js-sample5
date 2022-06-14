from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer

def hello(request):
    queryset = Customer.objects.annotate(is_new=True)
    
    return render(request, 'hello.html', {'queryset': queryset})
