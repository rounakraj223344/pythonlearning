p=1000
r=5
t=3
si=p*r*t/100
print(si)
p=1000
r=5
t=3
n=1
a=p*(1+r/100*n)**(n*t)
print(a)
compound_intrest=1000,3,5,10
p,r,t,n=compound_intrest
a=p*(1+r/100)**(n*t)
print(a)
a=input("enter string to check palindrome:")

if a[0]==a[3]:
    if a[1]==a[2]:
        print("it is a palindrome")
    else:
        print("not a palindrome")
else:
    print("not a pandildome")

