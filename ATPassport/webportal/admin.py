from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User, AtUser, LoanInstance, Equipment, Provider, AtCategory


# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(AtUser)
admin.site.register(LoanInstance)
admin.site.register(Equipment)
admin.site.register(Provider)
admin.site.register(AtCategory)
