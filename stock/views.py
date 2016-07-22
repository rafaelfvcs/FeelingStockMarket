from django.http import Http404
from django.shortcuts import render
from .models import Stock


def index(request): # oareu de atualizar 13 - 1:40 min
    all_stocks = Stock.objects.all()
    context = {'all_stocks': all_stocks}
    return render(request, 'stock/index.html', context)

def detail(request, stock_id):
    try:
        stock = Stock.objects.get(pk=stock_id)
    except Stock.DoesNotExist:
        raise Http404('Stock does not exist!')
    return render(request, 'stock/detail.html', {'stock': stock})