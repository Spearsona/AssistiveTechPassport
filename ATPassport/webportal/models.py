from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    pass

# Create your models here.
class AtUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key= True)

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField('Date Of Birth')
    email = models.EmailField

    def __str__(self):
        return self.firstName + " " + self.lastName 

#Single Provider user account will be linked to each Loan. 
class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key= True)
    name = models.CharField(max_length=100)

    #Could potentially make this contain a list of staff users as well as part of group permissions. 

    def __str__(self):
        return self.name

class AtCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    @classmethod
    def create(cls):
        category = cls(name='generic', desc='generic')
        category.save()
        return category



class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    atcategory = models.ForeignKey(AtCategory, on_delete=models.CASCADE)
    inventory = models.IntegerField(default= 10)

    def __str__(self):
        return self.name
    
    @classmethod
    def create(cls, name, description, atcategory, inventory):
        equipment = cls(name=name, description=description, atcategory=atcategory, inventory=inventory)
        return equipment

   
    
class LoanInstance(models.Model):
    due_date = models.DateField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    atuser = models.ForeignKey(AtUser, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    @property
    def is_overdue(self):
        """Check whether the Loan is overdue based on due date and current date."""
        return bool(self.due_date and date.today() > self.due_date)
    
    


    class Meta:
        permissions = (("can_return", "Can set loan as returned"),)


