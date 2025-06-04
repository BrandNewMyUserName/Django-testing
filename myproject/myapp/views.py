from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {'name': "Illia"}
    return render(request, 'index.html', context)

def base_ext(request):
    return render(request, 'base_ext.html')

def base_view(request):
    return render(request, 'base.html')