from django import forms

from smartphone.models import Smartphone

class SmartphoneForm(forms.ModelForm):
    model = Smartphone
    fields = '__all--'

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError("El precio debe ser mayo a 0")

        return price

