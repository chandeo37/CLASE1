from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com'
        })
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': "form-control",
            "row": 3
        })
    )
    firstName = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        })
    )
    lastName = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )

    #COUNTRIES = [
     #   ('CL', 'Chile'),
     #   ('VE', 'Venezuela'),
     #   ('AR', 'Argentina'),
     #   ('US', 'E.E.U.U')
    #]
    #agregar los campos del formulario
   # name = forms.CharField(label='Name', max_length=400)
    #email = forms.EmailField()
    #age = forms.IntegerField(label='Age', min_value=1)
    #select
    #country = forms.ChoiceField(choices=COUNTRIES)
    #seleccion multiple
    #countries_extra = forms.MultipleChoiceField(choices=COUNTRIES)