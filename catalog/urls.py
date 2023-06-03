from operator import index

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product, contacts, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)