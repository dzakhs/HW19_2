from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

     def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        censored_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in censored_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(f'Запрещено использовать слово "{word}" в названии или описании продукта.')
        return cleaned_data

     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field_name, field in self.fields.items():
             field.widget.attrs['class'] = 'form-control'

     class Meta:
         model = Product
         fields = '__all__'





class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


    #def clean_is_version(self):
    #    is_version = self.cleaned_data.get('is_version')
    #    product = self.cleaned_data.get('product')
#
    #    Version.objects.filter(product=product).exclude(id=self.instance.id).update(is_version=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'