print("BIRTHDAY CELEBRATION")
age=int(input("enter the age of a person :"))
num=int(input("enter list length :"))
if age==num:
    list=[]
    for i in range(num):
        candle_heights=int(input("enter candle heights:"))
        list.append(candle_heights)
    print("candle heights are :",list)
    n=max(list)
    count=0
    j=0
    while (j<len(list)):
        if (list[j]==n):
            count=count+1
        j+=1
    print("maximum height of candle : ",n,"\n","number of maximum height of candle : ",count )
else:
    print("check the details what you enter  ,age not match with no of candles ")


