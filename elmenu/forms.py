from django import forms

class orderForm(forms.Form):
    pizza = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'What flavor would you like to heve?'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'What is your name?'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Where should we deliver it?'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Please enter your phone number?'}))