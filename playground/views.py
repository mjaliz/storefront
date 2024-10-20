from django.shortcuts import render
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = OrderItem.objects.filter(product__collection__id=3)
    for c in queryset:
        print(c)
    return render(request, "hello.html", {"name": "Mosh"})
