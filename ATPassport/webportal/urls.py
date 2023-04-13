from django.urls import path

from . import views
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('providerloans', views.providerloans, name='providerloans'),
    path('userloans', views.userloans, name='userloans'),
    
]

#Remove for production enviornment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


