from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Customer

class CustomerSignUpForm(UserCreationForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address'}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.address = self.cleaned_data.get('interests')
        
        return user