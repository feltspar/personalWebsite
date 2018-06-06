from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'dala':"Ye le"}
    return render(request, 'resume_app/index.html', context=my_dict)
