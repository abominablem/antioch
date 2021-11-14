from django.shortcuts import render
from django.views import generic

# Create your views here.

def import_view(request):
    return render(request, 'import_view.html', context = {})