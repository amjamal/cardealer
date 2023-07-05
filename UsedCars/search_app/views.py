from django.shortcuts import render
from carapp.models import Car
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    cars = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        cars = Car.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'cars': cars})
