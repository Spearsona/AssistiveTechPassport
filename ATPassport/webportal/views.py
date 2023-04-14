from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import AtUser, LoanInstance, Provider, Equipment
app_name = 'webportal'

def index(request):
    context={}
    return render(request, 'webportal/index.html', context) 

@login_required
def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    atuserid = request.user.id
    atuser = AtUser.objects.get()
    
    userloans = LoanInstance.objects.filter(atuser=atuserid)

    num_userloans = userloans.count()

    context={
        'atuser': atuser,
        'userloans': userloans,
        'num_userloans': num_userloans,
    }
    return render(request, 'webportal/userloans.html', context)

@login_required
def providerloans(request):
    provideruser = request.user
    provideruser = Provider.objects.get(pk=provideruser)
    providerloans = LoanInstance.objects.filter(provider=provideruser)
    

    context ={
        'provider': provideruser,
        'providerloans': providerloans,
        
    }
    return render(request, 'webportal/providerloans.html', context)

def Catalog(request):
    context={
    }
    return render(request, 'webportal/catalog.html', context)

    
class EquipmentListView(ListView):
    model = Equipment
    paginate_by: 20


