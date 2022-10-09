from django.urls import path

from . import views

app_name = 'potentialleads'
urlpatterns = [
    
    path('Import_csv/', views.Import_csv,name="Import_csv"), 
]