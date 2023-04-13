from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AtUser, LoanInstance
app_name = 'webportal'

def index(request):
    context={}
    return render(request, 'webportal/index.html', context) 


def userloans(request):
    #userid will be taken from session, putting in placeholder user for now
    atuserid = 1
    
    atuser = AtUser.objects.get(user_id=1)
    
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
    pass

