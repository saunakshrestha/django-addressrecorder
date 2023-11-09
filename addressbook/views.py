from django.shortcuts import render,redirect
from .models import AddressBookEntry
from .form import AddressEntryForm
#from django.http import HttpResponseRedirect
# Create your views here.
def welcome_page(request):
    return render(request,'addressbook/welcome.html')

def list_entries(request):
    address_entries = AddressBookEntry.objects.all()
    context = {
        "address_entries" : address_entries
    }
    return render(request,'addressbook/home.html',context)
def address_entry_form(request):
    entry_form = AddressEntryForm()
    if (request.method=='POST'):
        entry_form = AddressEntryForm(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('list_entries')
        else:
            entry_form = AddressEntryForm()

    context = {
        'form': entry_form,
    }
    return render(request,'addressbook/address.html',context)