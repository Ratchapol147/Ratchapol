from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import datagithub,imgcertificate
from django_distill import distill_path

def index (request):
    data = datagithub.objects.all()
    img = imgcertificate.objects.all()
    return render(request,'index.html',{'data':data,'img':img})

