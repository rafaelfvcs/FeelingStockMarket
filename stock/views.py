from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is my second homepage STOCK</h1>')
