from django.shortcuts import render
from .utils import *
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        Util.contactemail(request,email)
        messages.info(request,'Your Inquiry Successfully...')
    return render(request,'webapp/index.html')

def ourbank(request):
    return render(request,'webapp/our_bank.html')

def research(request):
    return render(request,'webapp/investment_research.html')

def financing(request):
    return render(request,'webapp/financing_products.html')

def errorpage(request):
    return render(request,'webapp/errorpage.html')

# en folder
def enfinance(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-13]
    return render(request,'webapp/EN/financing_products.html',{'selectedFolder':selectedFolder})

def eninvestment(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/EN/investment_research.html',{'selectedFolder':selectedFolder}) 

def enourbank(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/EN/our_bank.html',{'selectedFolder':selectedFolder}) 

# de folder
def definance(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-13]
    return render(request,'webapp/DE/financing_products.html',{'selectedFolder':selectedFolder})

def deinvestment(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/DE/investment_research.html',{'selectedFolder':selectedFolder}) 

def deourbank(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/DE/our_bank.html',{'selectedFolder':selectedFolder}) 

# cz folder
def czfinance(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-13]
    return render(request,'webapp/CZ/financing_products.html',{'selectedFolder':selectedFolder})

def czinvestment(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/CZ/investment_research.html',{'selectedFolder':selectedFolder}) 

def czourbank(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/CZ/our_bank.html',{'selectedFolder':selectedFolder}) 

# es folder
def esfinance(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-13]
    return render(request,'webapp/ES/financing_products.html',{'selectedFolder':selectedFolder})

def esinvestment(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/ES/investment_research.html',{'selectedFolder':selectedFolder}) 

def esourbank(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/ES/our_bank.html',{'selectedFolder':selectedFolder}) 

# tr folder
def trfinance(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-13]
    return render(request,'webapp/TR/financing_products.html',{'selectedFolder':selectedFolder})

def trinvestment(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/TR/investment_research.html',{'selectedFolder':selectedFolder}) 

def trourbank(request):
    current_url = request.build_absolute_uri()
    selectedFolder = current_url[22:-14]
    return render(request,'webapp/TR/our_bank.html',{'selectedFolder':selectedFolder}) 



def lang(request,selectedFolder):
    if selectedFolder=="CZ":
        return render(request,'webapp/CZ/index.html',{'selectedFolder':selectedFolder})
    
    elif selectedFolder=="DE":
        return render(request,'webapp/DE/index.html',{'selectedFolder':selectedFolder})

    elif selectedFolder=="EN":
        return render(request,'webapp/EN/index.html',{'selectedFolder':selectedFolder})

    elif selectedFolder=="ES":
        return render(request,'webapp/ES/index.html',{'selectedFolder':selectedFolder})

    elif selectedFolder=="TR":
        return render(request,'webapp/TR/index.html',{'selectedFolder':selectedFolder})
    
    