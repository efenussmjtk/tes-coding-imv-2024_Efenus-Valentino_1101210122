num=int(input("masukan bilangan:"))
temp=1
k=0
a=0
summ=0
while summ<=num:
    summ=temp+k
    temp=summ
    k=temp
    if summ==num:
        a=a+1
        print("angka {} merupakan angka fibonacci".format(num))
        break
if a==0:
    print("angka {} bukan merupakan angka fibonacci".format(num))