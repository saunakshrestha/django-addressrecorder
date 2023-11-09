from django import forms
from .models import AddressBookEntry


class AddressEntryForm(forms.ModelForm):
    class Meta:
        model = AddressBookEntry
        fields = "__all__"
    name = forms.CharField(label='name',max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your full name:'}))
    address = forms.CharField(label='address',max_length=50,widget=forms.TextInput(attrs={'placeholder':'Enter your. address:'}))


    
