from django import forms

from catalog.models import Product


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

     class Meta:
         model = Product
         fields = '__all__'
