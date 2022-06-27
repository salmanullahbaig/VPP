from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import  User_Message_form
from affilate.models import user_wallet , user_seed
from accounts.models import Refer
from django.contrib import messages
from .transfer import *

#from affilate.utils import plan_age

@login_required
def home(request):
    total_seed =0
    total_seed = total_seeds()
    seed_left = 10000 - total_seed
    user_seed = total_user_seeds(request)
    print("total seed ", total_seed, "user seed", user_seed)
    return render(request, 'home.html', locals())
@login_required
def Purchase_seed(request):
    return render(request, 'dashboard.html', locals())

def total_user_seeds(request):
    try:
        total_seed_list = user_seed.objects.filter(user = request.user)
        seed_counter = 0
        for seed in total_seed_list:
            seed_counter += int(seed.seed)
    except Exception as e:
        print(e)
        seed_counter=0
    return seed_counter

def total_seeds():
    total_seed_list = user_seed.objects.all()
    seed_counter = 0
    for seed in total_seed_list:
        seed_counter += int(seed.seed)
    return seed_counter


# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')

@login_required
def walletView(request):
    try:
        api_keys  = user_wallet.objects.get(user = request.user).get_api()
        public_key, secret_key = api_keys['public_key'], api_keys['secret_key']
    except:
        public_key, secret_key = "kk3j4234j3lk343434324j32", "343k4j343243243243343243243"
    form= User_Message_form()
    return render(request, 'wallet.html', locals())
@login_required
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

@login_required
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


trx_limit = 100
@login_required
def add_one_seed(request):
    print("Adding one seed")
    seed_value = 1
    trx = get_trx_user(request.user)
    usdt = get_usdt_user(request.user)
    print("Trx",trx,"usdt=", usdt)
    if usdt >= seed_value and trx > trx_limit:
        try:
            distrubute_refer_bonus(request.user, seed_value)
            messages.success(request, 'Distrubution successfully')
            user_seed.objects.create(user = request.user, seed = 1,status = "paid", seed_value= seed_value )
        except:
            messages.error(request, 'Distrubution is not successful')
    elif trx < trx_limit:
        messages.error(request, 'Please add TRX, there is only '+str(trx) + " in your account")
    elif usdt < seed_value:
        messages.error(request, 'Please add USDT, there is only '+str(trx) + " in your account")
    return render(request, 'dashboard.html', locals())
@login_required
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

@login_required
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
