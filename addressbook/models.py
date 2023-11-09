from django.db import models

# Create your models here.

class AddressBookEntry(models.Model):
    class Meta:
        verbose_name_plural = "AddressBookEntries"
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return self.name