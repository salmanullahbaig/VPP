
from django.contrib import admin
from django.urls import path , include
from . import views
from accounts import urls as accounts_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name= 'index'),
    path('purchase_seed',views.Purchase_seed,name= 'purchase_seed'),
    path('wallet/',views.walletView,name= 'wallet'),
    path('message/',views.sendMessageView,name= 'message'),
    #path('refers/',views.refersView, name= 'refers'),
    path('refer_link/',views.affilateLinkView, name= 'refer_link'),
    path('account/',include(accounts_urls)),

    path('one_seed/',views.add_one_seed,name= 'one_seed'),
    path('two_seed/',views.add_2_seed,name= 'two_seed'),
    path('add_10_seed/',views.add_10_seed,name= 'add_10_seed'),
    path('add_100_seed/',views.add_100_seed,name= 'add_100_seed'),
    path('add_200_seed/',views.add_200_seed,name= 'add_200_seed'),


]
