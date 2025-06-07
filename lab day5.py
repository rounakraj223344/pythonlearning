"""a=[10,20,30,40,50]
b=a[0:4]
c=sum(a[0:4])
print(b)
print(c)"""

"""a=[10,20,30,40,51]
if a[4]%2==0:
    print("even")
else:
    print("odd")"""


"""list=[10,20,30,40,50,60,70,70,80,90,100]
print(list[2:8])
c=0
for x in list[4:8]:
    print(x**2)
    c=c+x**2
print(c)"""


a=[]
for x in range(6):
    b=input("enter number:")
    a.append(b)
    print(max(a[2:5]))
