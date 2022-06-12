from accounts.models import Refer

def make_transcation(user, amount):
    print("Adding ", amount , " to ", user)
    pass

def distrubute_refer_bonus(user, total_amount):
    ref_tree = Refer.objects.get(user = user)
    ref_by = ref_tree.recommended_by
    #Checking refer_uptill_top
    counter = 1
    while ref_by.username != 'superuser':
        if counter ==1:
            #Direct Refer
            amount_add = (10 * total_amount)/100
            make_transcation(user, amount_add)
            print("Adding amount ", amount_add)
            #Adding the bonus to database
            bonus_instance = User_Bonus_Model(user=user,bonus=bonus_name, amount=amount_add , percentage=percentage, total_value= total_amount,comment = reason )
            bonus_instance.save()
            print("saved")
            #bonus for first user
            pass
        if counter == 2:
            pass
        if counter == 3:
            pass
        if counter == 4:
            pass
        counter +=1
        ref_by = ref_tree.recommended_by
