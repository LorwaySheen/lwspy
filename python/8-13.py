def func1(firstname,lastname,**whatin):
    whatin['first_name'] = firstname
    whatin['last_name'] = lastname
    for key,value in whatin.items():
        print(key + ' ' + value)
        

func1('george',"bush",sex="male",age='old')


