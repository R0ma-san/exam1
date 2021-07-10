def func(a):
    d = {}
    for i in a:
        if type(i)==bool:
            d['bool'] = i
        elif type(i)==int:
            d['int']=i
        elif type(i)==float:
            d['float']=i
        elif type(i)==None:
            d['None']=i
        elif type(i)==str:
            d['str']=i
    return d

l = [1, 4.7, 'hi', False, None]
l1 = [True, 2.3, None, 'brook', 5]
print(func(l))
print(func(l1))
