'''def numer(a):
    return a**2
print(numer(3))'''
'''def scors(list_1:list,count:int,total:int) -> list:
    x,n=0,0
    g=list(filter(lambda y:y>=80,list_1))
    o=len(g)
    h=sum(g)
    count+=o
    total+=h
    avg=total/count
    print(f'{count / len(list_1):.1%}')
    return
scors([85,90,78,92,88],0,0)'''
'''text='Hello python'
a=sum(map(lambda x:ord(x),text))
print(a)'''
'''numer=[i for i in range(101) if i/3 
and i/5==0 
and i**3/2==0 
and any('4'  in '' for x in i)]
print(numer)'''
'''data={'a':5,'b':2,'c':8,'d':1}
a=sorted(data,key=data.get)[0:3]
print(a)'''
'''def make_math_func(numer):
    def nowfunc(mi):
        print(mi**numer)
    return nowfunc
square = make_math_func(2)
square(2)'''
numer=[]
print(numer)


