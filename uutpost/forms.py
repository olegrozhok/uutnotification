from django import forms
from .models import Address


class AddAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name_addr', 'mobile_addr', 'vk_addr', 'tg_addr', 'management_company']


# class AddManagement(forms.ModelForm):
#     class Meta:
#         model = Management
#         fields = ['name_man', 'mobile_man', 'vk_man', 'tg_man']

