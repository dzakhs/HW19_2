from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic

from catalog.models import Product, Contacts, Blog


class IndexListView(generic.ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductListView(generic.ListView):
    model = Product



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

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)

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



