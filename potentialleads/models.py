
from django.db import models



class Lead(models.Model):    
    lead = models.CharField(max_length=150, null=False)
    id = models.IntegerField(primary_key=True,editable=False)
    services = models.CharField(max_length=100,null=False)    
    domain = models.CharField(max_length=100,null=False)
    channels = models.CharField(max_length=100,null=False)
    stage = models.CharField(max_length=20,null=False)
    status = models.CharField(max_length=20,null=False) 
    amount = models.IntegerField(null=False)        
    saleRepresentative = models.CharField(max_length=50, null=False)
    created_at = models.DateField(null=False, blank=False) 
    signed_at = models.DateField(null=True, blank=True) 
    closed_at = models.DateField(null=True, blank=True) 
    def __str__(self):
        return self.lead

