from django.db import models
from example_app.models import BakedGood, ModelForm

class Order(models.Model): 
    items = models.ManyToManyField(BakedGood)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['items']
