from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Blog, Version


class IndexListView(generic.ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductListView(generic.ListView):
    model = Product

class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST)
        else:
            formset = VersionFormset()

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)
class ProductDetailView(generic.DetailView):
    model = Product


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

class ContactsListView(generic.ListView):
    model = Contacts
    template_name = 'catalog/contact.html'


class BlogListView(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(is_published=True)


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('name', 'content', 'image', 'is_published')
    success_url = reverse_lazy('catalog:blog_list')



class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self, queryset=Blog):
        object = super().get_object()
        object.view_count += 1
        object.save()
        return object


class BlogUpdateView(generic.UpdateView):
    model = Blog

    fields = ['name', 'content', 'image']
    success_url = reverse_lazy('catalog:blog_list')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('catalog:blog_detail', kwargs={'pk': pk})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

#def product(request):
#    product_list = Product.objects.all()
#    content = {
#        'object_list': product_list
 #   }
 #   return render(request, 'catalog/product.html', content)


#def contacts(request):
#    return render(request, 'catalog/contact.html')

#def index(request):
#    product_list = Product.objects.all()
#    context = {
#        'object_list': product_list
#    }
#    return render(request, 'catalog/index.html', context)



