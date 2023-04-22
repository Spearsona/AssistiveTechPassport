from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.list import ListView
from .models import AtUser, LoanInstance, Provider, Equipment, AtCategory
from .forms import CreateEquipmentForm
from django.http import HttpResponseRedirect
from datetime import datetime
from dateutil.relativedelta import relativedelta

app_name = 'webportal'

@login_required
def index(request):
    context={}
    return render(request, 'webportal/index.html', context) 

@login_required
def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    atuserid = request.user.id
    atuser = AtUser.objects.get(user_id=atuserid)
    
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
    provider = Provider.objects.get(pk=provideruser)
    providerloans = LoanInstance.objects.filter(provider=provider)
        
    context ={
        'provider': provideruser,
        'providerloans': providerloans,
    }
    return render(request, 'webportal/providerloans.html', context)


@login_required
def EquipmentListView(request): 

    def DeleteEquipment(request, obj_id):
        object = get_object_or_404(Equipment, pk=obj_id)
        object.delete()

    if request.method == 'POST':
        createform = CreateEquipmentForm(request.POST)
        if createform.is_valid():
            print(createform.cleaned_data) 
            # data = form.cleaned_data['name']
            # print(data);
            cd = createform.cleaned_data
            provideruser = request.user
            provider = Provider.objects.get(pk=provideruser)
            catString = createform.cleaned_data['atcategory']
            
            eq = Equipment.create(createform.cleaned_data['name'],
                                  createform.cleaned_data['description'],
                                  AtCategory.objects.get(name=catString),
                                  createform.cleaned_data['inventory'],
                                  provider,
                                  createform.cleaned_data['imgsrc'])
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

@login_required
# @permission_required('catalog.can_mark_returned', raise_exception=True)
def delete_Equipment(request, id):
    print("IN DELETE")
    equipment = get_object_or_404(Equipment, pk=id)
    equipment.delete()
    return HttpResponseRedirect("/webportal/equipment")


@login_required
@permission_required('webportal.add_loaninstance', raise_exception=True)
def loanEquipment(request, id):
    print("Im loaning some equipment")
    equipment = get_object_or_404(Equipment, pk=id)
    if equipment.inventory > 0: 
        equipment.inventory = equipment.inventory - 1
        threemonthstime = datetime.today() + relativedelta(months=3)
        
        atuserid = request.user
        print(atuserid)
        atuser = AtUser.objects.get(pk=atuserid)
        loaninstance = LoanInstance.create(due_date=threemonthstime, equipment=equipment, atuser=atuser, provider=equipment.provider)
        
        loaninstance.save()
        equipment.save()
        return HttpResponseRedirect("/webportal/userloans")

    else:
        raise Exception("Inventory not sufficent to loan this equipment")
    
   
    


