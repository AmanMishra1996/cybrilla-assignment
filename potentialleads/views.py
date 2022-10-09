
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.utils import timezone
from django.core.files.storage import FileSystemStorage
import pandas as pd

from datetime import datetime

from .models import Lead

def Import_csv(request):
                 
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                obj = Lead.objects.create(lead=dbframe.Lead,
                                            id=dbframe.ID, 
                                            services=dbframe.Services,
                                            domain=dbframe.Domain, 
                                            channels=dbframe.Channels, 
                                            stage=dbframe.Stage,
                                             status=dbframe.Status, 
                                            amount=dbframe.Amount, 
                                            saleRepresentative=dbframe._9, 
                                            created_at=datetime.strptime(dbframe.Created_at,'%d-%m-%Y').date().strftime("%Y-%m-%d"),
                                            signed_at= None if pd.isna(dbframe.Signed_at) else datetime.strptime(dbframe.Signed_at,'%d-%m-%Y %H:%M' if len(dbframe.Signed_at)>11 else '%d-%m-%Y').date().strftime("%Y-%m-%d"),
                                            closed_at=None if pd.isna(dbframe.Closed_at) else datetime.strptime(dbframe.Closed_at,'%d-%m-%Y').date().strftime("%Y-%m-%d"))

                obj.save()
 
            return render(request, 'potentialleads/importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'potentialleads/importexcel.html',{})           