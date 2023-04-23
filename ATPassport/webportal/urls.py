from django.urls import path
from .views import EquipmentListView

from . import views
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('providerloans', views.providerloans, name='providerloans'),
    path('userloans', views.userloans, name='userloans'),
    path('equipment', views.EquipmentListView, name='equipment'),
    path('equipmentdelete/<int:id>',views.delete_Equipment, name='equipmentdelete'),
    path('loanEquipment/<int:id>',views.loanEquipment, name='loanEquipment'),
    path('returnEquipment/<int:id>',views.returnEquipment, name='returnEquipment')

]

#Remove for production enviornment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


