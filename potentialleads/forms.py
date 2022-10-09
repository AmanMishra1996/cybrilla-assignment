from django import forms
 
 
from .models import Lead
 
class UploadLeadData(forms.ModelForm):
    class Meta:
        model = Lead
        fields =[ 'lead','id','','services','domain','channels' ,'stage','status',
                  'amount','saleRepresentative','created_at','signed_at','closed_at'
        ] 