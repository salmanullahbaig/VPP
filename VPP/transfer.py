from accounts.models import Refer
from affilate.models import user_wallet , user_bonus as User_Bonus_Model
from django.contrib.auth.models import User

#!pip install tronpy
from tronpy import Tron
from tronpy.keys import PrivateKey
import time
from affilate.models import User_transcations, user_wallet, user_seed

company_username= 'superuser'
superuser =  User.objects.get(username= company_username)

def make_transcation(from_user, to_user, amount):
    print("Trying to Add from ", from_user, amount , " to ", to_user)
    try:
        transfer_usdt(from_user, to_user, amount)
        print("Added ", amount , " to ", to_user)
    except Exception as e:
        print("line 20", e)
        pass

def distrubute_refer_bonus(user, total_amount):
    ref_tree = Refer.objects.get(user = user)
    ref_by = ref_tree.recommended_by
    print(ref_by)
    #Checking refer_uptill_top
    counter = 1
    percentage_used = 0
    while True:
        if counter ==1:
            if ref_by.username == company_username:
                make_transcation(user ,ref_by, total_amount)
                percentage_used=100
                break
            else:
                #Direct Refer
                amount_add = (10 * total_amount)/100
                make_transcation(user, ref_by, amount_add)
                print("Adding amount ", amount_add)
                percentage_used=10
                #Adding the bonus to database
                bonus_name = 'Referal bonus11'
                bonus_instance =  User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add  )
                bonus_instance.save()
                print("saved", counter)
                #bonus for first user

        if counter == 2:
            if ref_by.username == company_username:
                percent =100 - percentage_used
                amount_add = (percent * total_amount)/100
                make_transcation(user ,ref_by, amount_add)
                percentage_used=100
                break
            else:
                #Direct Refer
                amount_add = (5 * total_amount)/100
                make_transcation(user, ref_by, amount_add)
                print("Adding amount ", amount_add)
                percentage_used=percentage_used + 5
                #Adding the bonus to database
                bonus_name = 'Referal bonus1'
                bonus_instance =  User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add  )
                bonus_instance.save()
                print("saved", counter)
                #bonus for first user

        if counter == 3:
            if ref_by.username == company_username:
                percent =100 - percentage_used
                amount_add = (percent * total_amount)/100
                make_transcation(user ,ref_by, amount_add)
                percentage_used=100
                break
            else:
                #Direct Refer
                amount_add = (5 * total_amount)/100
                make_transcation(user, ref_by, amount_add)
                print("Adding amount ", amount_add)
                percentage_used=percentage_used + 5
                #Adding the bonus to database
                bonus_instance =  User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add  )
                bonus_instance.save()
                print("saved", counter)
                #bonus for first user
        if counter == 4:
            if ref_by.username == company_username:
                percent =100 - percentage_used
                amount_add = (percent * total_amount)/100
                make_transcation(user ,ref_by, amount_add)
                percentage_used=100
                break
            else:
                #Direct Refer
                amount_add = (5 * total_amount)/100
                make_transcation(user, ref_by, amount_add)
                print("Adding amount ", amount_add)
                percentage_used=percentage_used + 5
                #Adding the bonus to database
                bonus_instance =  User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add  )
                bonus_instance.save()
                print("saved", counter)
                #bonus for first user

        if counter == 5:
            percent =100 - percentage_used
            amount_add = (percent * total_amount)/100
            make_transcation(user ,superuser, amount_add)
            percentage_used=100
            break

        counter +=1
        ref_tree = Refer.objects.get(user = ref_by)
        ref_by = ref_tree.recommended_by



client = Tron()
"""
from tronpy.providers import HTTPProvider
# Use private network as HTTP API endpoint
client = Tron(HTTPProvider("http://127.0.0.1:8090"))
"""

# create a Tron wallet and print out the wallet address & private key
def create_wallet():
    wallet = client.generate_address()
    print("Wallet address:  %s" % wallet['base58check_address'])
    print("Private Key:  %s" % wallet['private_key'])
    return wallet['base58check_address'] , wallet['private_key']


#public_key,  private_key = create_wallet()
def get_trx_balance(address):
    balance = client.get_account_balance(str(address))
    return balance

def get_trx_user(user):
    try:
        from_user_api = user_wallet.objects.get(user = user).get_api()
        from_adress = from_user_api['public_key']
        #priv_key = from_user_api['secret_key']
        balance = client.get_account_balance(str(from_adress))
    except:
        balance= 0
    return balance
def get_usdt_user(user):
    try:
        from_user_api = user_wallet.objects.get(user = user).get_api()
        from_adress = from_user_api['public_key']
        #priv_key = from_user_api['secret_key']
        CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
        cntr = client.get_contract(CONTRACT)
        precision = cntr.functions.decimals()
        balance = cntr.functions.balanceOf(from_adress) / 10 ** precision
    except:
        balance= 0
    return balance




def get_usdt_balance(adress):
    "Return the balance of the user wallet in USDT"
    CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    cntr = client.get_contract(CONTRACT)
    precision = cntr.functions.decimals()
    return cntr.functions.balanceOf(adress) / 10 ** precision

def transfer_usdt(from_user, to_user, amount):

    try:
        from_user_api = user_wallet.objects.get(user = from_user).get_api()
        from_adress = from_user_api['public_key']
        priv_key = from_user_api['secret_key']
        to_adress = user_wallet.objects.get(user = to_user).get_api()['public_key']
    except Exception as e:
        print("Error in Wallet key :", e)
        return 0

    CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    print("Creating request for transfer on tron")
    contract = client.get_contract(CONTRACT) #("THi2qJf6XmvTJSpZHc17HgQsmJop6kb3ia")

    #amount = amount *1000000
    amount_send = int(amount  * 1000000)
    print("********* Sending ", amount, "  --", amount_send, "from = ",from_user, '__To=', to_user)
    #amount_send, balance

    try:
        is_trx_successful = False
        User_transcations.objects.create(user= from_user, amount = amount, from_user = from_user, credited = False)
        txn = (contract.functions.transfer(to_adress,  amount_send).with_owner(from_adress)  # address of the private key
               .fee_limit(5_000_000)
               .build()
               .sign(priv_key))
        time.sleep(5)# waiting for the transfer
        #User_transcations.objects.create()
        result =  txn.broadcast().result()
        is_trx_successful = True
    except Exception as e:
        print("issue is :", e)
    if is_trx_successful:
        User_transcations.objects.create(user= from_user, amount = amount, from_user = from_user, credited = True)
    else:
        User_transcations.objects.create(user= from_user, amount = amount, from_user = from_user, credited = False)
    print("Transfer completed")
    return result
