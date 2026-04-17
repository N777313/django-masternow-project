
from django.shortcuts import render, redirect
from .models import Order

from .forms import OrderForm

def dashboard(request):
    orders = Order.objects.all().order_by('-date_creation')
    return render(request, 'orders/dashboard.html', {'orders': orders})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            # статус и дата уже задаются в модели автоматически
            order.save()

            return redirect('dashboard')

    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})
