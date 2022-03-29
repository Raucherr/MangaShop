from django import forms

from main.models import Manga
from order.models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        print(phone)
        if not phone.startswith('+996'):
            raise forms.ValidationError('Номер должен начинаться с +996')
        if len(phone) != 13:
            raise  forms.ValidationError('Неправильный номер')
        return phone