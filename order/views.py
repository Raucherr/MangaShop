from django.http import HttpResponse
from django.shortcuts import render

from .forms import CreateOrderForm
from .models import Order


def create_order(request):
    print(request.POST)
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save( )
        return render(request, 'order/order.html', {'form': order_form})
    order_form = CreateOrderForm()
    return render(request, 'order/order.html', {'form': order_form})
