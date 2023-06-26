from operator import index

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsListView, IndexListView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductUpdateView, ProductDeleteView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name





urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('product/', ProductListView.as_view(), name='product'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)