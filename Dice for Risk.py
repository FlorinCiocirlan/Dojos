def att_dices(x,y):
    Att_list=[]
    import random
    for i in range(3):
        Att_list.append(random.randrange(x,y))
    Att_list.sort(reverse=True)
    print("Zarurile atacator:",Att_list)
    return def_dices(1,6)


def def_dices(x,y):
    Def_list=[]
    import random
    for i in range(2):
        Def_list.append(random.randrange(x,y))
    Def_list.sort(reverse=True)
    print("Zarurile aparare :",Def_list)
    return def_dices(1,6)



""" if sum(Att_list) > sum(Def_list)
    print("Defender lost 1 unit")
elif att_dices(1,6) == def_dices(1,6):
    print("Attacker lost 1 unit")
elif att_dices(1,6) < def_dices(1,6):
    print("Attacker lost 1 unit")
 """