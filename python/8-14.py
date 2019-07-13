def fun1(maker,model,**others):
        others['maker'] = maker
        others['model'] = model
        for key,value in others.items():
                others[key] = value
        return others

car1 = fun1('BENZ',"S600",price = '3,000,000',length = '5m')
print(car1)

