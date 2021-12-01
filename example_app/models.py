from django.db import models
from django.forms import ModelForm

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    
class BakedGood(models.Model): 
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.CharField(
        max_length=2,
        choices=[
            ('BG',"Bagel"),
            ('BR',"Bread"),
            ('CO',"Cookie"),
            ('CA',"Cake"),
            ('PR',"Pretzel")
        ],
        default='BG',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    baked_on = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    def make_json(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "price": self.price,
        }

class BakedGoodForm(ModelForm):
    class Meta:
        model = BakedGood
        fields = ['name', 'desc', 'good_type', 'price', 'recipe', 'ingredients', 'baked_on']