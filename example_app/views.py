from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions

from .models import BakedGood, BakedGoodForm, Ingredient
from .serializers import BakedGoodSerializer, IngredientSerializer
    
def index(request):
    if 'q' in request.GET:
        query = request.GET['q']
    else:
        query =''
    baked_goods = BakedGood.objects.filter(name__icontains=query)
    return render(request, 'example_app/index.html', {'baked_goods': baked_goods})
    
def bake(request): 
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()

    return render(request, 'example_app/bake.html', {'form': form})
    
def pic(request):
    return render(request, 'example_app/pic.html')
    
def ajax_template(request):
    return render(request, 'example_app/ajax.html')
    
def ajax_demo(request):
    data = {}
    for baked_good in BakedGood.objects.all():
        data[baked_good.id] = baked_good.name
    return JsonResponse(data)
    
def auth(request):
    return render(request, 'example_app/auth.html')
    
class BakedGoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows baked goods to be viewed or edited.
    """
    queryset = BakedGood.objects.all()
    serializer_class = BakedGoodSerializer
    #permission_classes = []
    
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

