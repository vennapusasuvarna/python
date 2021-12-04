#take three user inputs ,print the middleone  task given by praharsitha
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if (a>=b)  and (a>=c) :
    if b>=c :
        print(b," is middle")
    else:
        print(c,"is middle")

elif(b>=c) :
    if(a>=c):
         print(a," is middle")
    else:
         print(c," is middle")
else:
    if(a>=b):
        print(a," is middle")
    else:
         print(b," is middle")
 
"""
enter first number:-67
enter second number:-34
enter third number:-23
34  is max

Global frame
a	67
b	34
c	23

"""






























































































































































































































































