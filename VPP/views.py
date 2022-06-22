from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import  User_Message_form
from affilate.models import user_wallet
from accounts.models import Refer
#from affilate.utils import plan_age

def home(request):
    form= User_Message_form()
    return render(request, 'index.html', locals())

    #return HttpResponse(qs_json, content_type='application/json')

def walletView(request):
    try:
        api_keys  = user_wallet.objects.get(user = request.user).get_api()
        public_key, secret_key = api_keys['public_key'], api_keys['secret_key']
    except:
        public_key, secret_key = "Not found", "Not found"
    form= User_Message_form()
    return render(request, 'wallet.html', locals())

def affilateLinkView(request):
    try:
        link  = Refer.objects.get(user= request.user).code
        link = "http://127.0.0.1:8000/account/sign-up/" + str(link)
    except:
        link = "Not_found"
    form= User_Message_form()
    return render(request, 'affilate_link.html', locals())


def refersView(request):
    try:
        api_keys  = user_wallet.objects.get(user = request.user).get_api()
        public_key, secret_key = api_keys['public_key'], api_keys['secret_key']
    except:
        public_key, secret_key = "Not found", "Not found"
    form= User_Message_form()
    return render(request, 'refers.html', locals())


def sendMessageView(request):
    if(request.POST):
        print(request.POST.dict())
        form= User_Message_form(request.POST)
        if form.is_valid():
            form.save()
        print(form)
        #return redirect('index')
        return render(request, 'index.html',locals())
    else:
        print(request.POST.dict())
        return render(request, 'index.html', locals())
