from django.shortcuts import render
from django.views import generic
from .ofx_parser import OFX

# Create your views here.

def import_view(request):
    return render(request, 'import_view.html', context = {})

def import_ofx(request):
    filename = None #TODO
    ofx_objects = {}
    # create an OFX object for each file imported
    for key, file in request.FILES.items():
        file_text = file.read()
        ofx_objects[file.name] = OFX().import_raw(file_text)
        file.close()
    context = {
        'ofx_objects': ofx_objects
        }
    # print(dir(ofx_objects[list(ofx_objects.keys())[0]]))
    # print(ofx_objects[list(ofx_objects.keys())[0]].transactions)
    return render(request, 'preview_files.html', context = context)