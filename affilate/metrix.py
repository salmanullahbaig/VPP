from accounts.models import Refer
from django.contrib.auth.models import User

company_username= 'superuser'

superuser = user.objects.get(username = company_username)

def make_transcation(from_user, to_user, amount):
    print("Adding ", amount , " to ", user)
    pass

def distrubute_refer_bonus(user, total_amount):
    ref_tree = Refer.objects.get(user = user)
    ref_by = ref_tree.recommended_by
    #Checking refer_uptill_top

    bonus_name = 'Referal bonus'
    reason =""
    percentage = 10
    counter = 1

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
                bonus_instance = User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add  )
                bonus_instance.save()
                print("saved")
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
                bonus_instance = User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add , percentage=percentage, total_value= total_amount,comment = reason )
                bonus_instance.save()
                print("saved")
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
                bonus_instance = User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add , percentage=percentage, total_value= total_amount,comment = reason )
                bonus_instance.save()
                print("saved")
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
                bonus_instance = User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add , percentage=percentage, total_value= total_amount,comment = reason )
                bonus_instance.save()
                print("saved")
                #bonus for first user

        if counter == 5:
            percent =100 - percentage_used
            amount_add = (percent * total_amount)/100
            make_transcation(user ,superuser, amount_add)
            percentage_used=100
            break

        counter +=1
        ref_by = ref_tree.recommended_by
