from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # def __init__(self,request,*args,**kwargs):
    #     super (OrderCreateForm,self).__init__(*args,**kwargs)
    #     self.fields['address'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address' }), initial=request.user.customer.address)
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address' }))
    postal_code = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'postal_code'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']