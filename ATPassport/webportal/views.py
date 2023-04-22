from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import AtUser, LoanInstance, Provider, Equipment, AtCategory
from .forms import CreateEquipmentForm
from django.http import HttpResponseRedirect

app_name = 'webportal'

@login_required
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

@login_required
def Catalog(request):
    context={
          'equipment': Equipment.objects,
    }
    return render(request, 'webportal/catalog.html', context)

@login_required
def EquipmentListView(request): 

    def DeleteEquipment(request, obj_id):
        object = get_object_or_404(Equipment, pk=obj_id)
        object.delete()

    if request.method == 'POST':
        createform = CreateEquipmentForm(request.POST)
        if createform.is_valid():
            print(createform.cleaned_data);
            # data = form.cleaned_data['name']
            # print(data);
            cd = createform.cleaned_data;
            catString = createform.cleaned_data['atcategory']
            
            eq = Equipment.create(createform.cleaned_data['name'],
                                  createform.cleaned_data['description'],
                                  AtCategory.objects.get(name=catString),
                                  createform.cleaned_data['inventory'])
            eq.save()
            return HttpResponseRedirect("/webportal/equipment")
    elif request.method == 'PUT':
        print("putputput")

    else:
        createform = CreateEquipmentForm
    context={
        'createform': createform,
          'equipment': Equipment.objects.all,
          'deletefunc': DeleteEquipment
    }
    return render(request, 'webportal/equipment_list.html', context)


