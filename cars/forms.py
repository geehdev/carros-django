from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_value(self):
        value = self.cleaned_data.get('value')
        print(value)
        print(self.cleaned_data)
        if value < 1:
            self.add_error(field='value', error='Valor mínimo do carro deve ser de R$1.00')

        return value






        