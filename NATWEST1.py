""" Problem Statement 
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for 
each year of their total age. They will only be able to blow out the tallest of the candles. Count how many 
candles are tallest. 
 
Example 
candles = [4, 4, 1, 3] 
The maximum height candles are 4 units high. There arbelow. 
birthdayCakeCandles has the following parameter(s): 
• int candles[n]: the candle heights 
Returns 
• int: the number of candles that are tallest 
Input Format 
The first line contains a single integer, n, the size of candles[]. 
The second line contains n space-separated integers, where each integer i describes the height of 
candles[i]. 
Sample Input 
 
4  
3 2 1 3 
a 
Sample Output    :        2 
Explanation 
Candle heights are [3, 2, 1, 3]. The tallest candles are 3 units, and there are 2 of them. e 2 of them, so return 2. 
"""
print("WELCOME TO BIRTHDAY CELEBRATION PARTY")
age=int(input("enter the age of a person :"))
n=int(input("enter list length :"))
if age==n:
    list=[]
    for i in range(n):
        candle_heights=int(input("enter candle heights:"))
        list.append(candle_heights)
    print("candle heights are :",list)
    maximum=0
    i=0
    while i<len(list):
        if list[i]>maximum:
            maximum=list[i]
        i+=1
    j=0
    count=0
    while (j<len(list)):
        if (list[j]==maximum):
            count=count+1
        j+=1
    print("maximum height of candle : ",maximum,"\n","number of maximum height of candle : ",count )
else:
    print("check the details what you enter  ,age not match with no of candles ")