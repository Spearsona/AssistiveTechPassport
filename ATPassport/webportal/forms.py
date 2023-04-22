from django import forms 
from .models import AtCategory, Equipment


class CreateEquipmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
    atcategories = AtCategory.objects.all()
    
    CATEGORIES = ()
    for item in atcategories:
        print(item.name, item.desc)
        CATEGORIES = CATEGORIES + ((item.name, item.name),)
 
    atcategory = forms.CharField(label='What is the category of this equipment?', widget=forms.Select(choices=CATEGORIES))
    inventory = forms.IntegerField()

    class Meta:
        model = Equipment
