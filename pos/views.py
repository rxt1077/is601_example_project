from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import OrderForm, Order

def order(request): 
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_cost = Decimal(0.00)
            for item in form.cleaned_data['items']:
                total_cost += item.price     
            
            order = form.save(commit=False)
            order.total_cost = total_cost
            order.save()
            form.save_m2m()
            
            #TODO: Redirect with pk to a view that shows total cost
            return HttpResponseRedirect(reverse('show_order', args=[order.id]))
    else:
        form = OrderForm()

    return render(request, 'pos/order.html', {'form': form})

def show_order(request, pk):
    order = Order.objects.get(id=pk)
    names = []
    for item in order.items.all():
        names.append(item.name)
    return render(request, 'pos/show_order.html', {'order': order, 'names': names})
