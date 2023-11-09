from django.urls import path
from .views import list_entries,address_entry_form,welcome_page

urlpatterns = [
    path('',welcome_page,name='welcome_page'),
    path('welcome/',welcome_page,name='welcome_page'),
    path('home/',list_entries,name='list_entries'),
    path('address/',address_entry_form,name='address_entry_form')
]
