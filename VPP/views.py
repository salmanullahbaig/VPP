from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import  User_Message_form
from affilate.models import user_wallet
from accounts.models import Refer
from django.contrib import messages
from .transfer import *
#from affilate.utils import plan_age

#@login_required
def home(request):
    form= User_Message_form()
    return render(request, 'home.html', locals())

def Purchase_seed(request):
    return render(request, 'dashboard.html', locals())

# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')


def walletView(request):
    try:
        api_keys  = user_wallet.objects.get(user = request.user).get_api()
        public_key, secret_key = api_keys['public_key'], api_keys['secret_key']
    except:
        public_key, secret_key = "kk3j4234j3lk343434324j32", "343k4j343243243243343243243"
    form= User_Message_form()
    return render(request, 'wallet.html', locals())

def affilateLinkView(request):
    try:
        link  = Refer.objects.get(user= request.user).code
        link = "http://127.0.0.1:8000/account/sign-up/" + str(link)
    except:
        link = "Not_found"
    users_tree = Refer.objects.filter(recommended_by=request.user)
    print(users_tree)
    users = []
    for tree in users_tree:
        users.append(tree.user)
    print(users)
    total_refers = len(users)
    return render(request, 'refferals.html', locals())


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


trx_limit = 50
def add_one_seed(request):
    print("Adding one seed")
    seed_value = 100
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, 100)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 1,status = "paid", seed_value= 100 )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())

def add_2_seed(request):
    print("Adding one seed")
    seed_value = 200
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, 200)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 2,status = "paid", seed_value= 200 )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())

def add_10_seed(request):
    print("Adding one seed")
    seed_value = 10 * 100
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, seed_value)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 10,status = "paid", seed_value= seed_value )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())

def add_100_seed(request):
    print("Adding one seed")
    seed_value = 100 * 100
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, seed_value)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 100,status = "paid", seed_value= seed_value )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())

def add_200_seed(request):
    print("Adding one seed")
    seed_value = 200 * 100
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, seed_value)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 200,status = "paid", seed_value= seed_value )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())
