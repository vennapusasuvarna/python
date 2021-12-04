"""Q3. Your local library needs your help! Given the expected and actual return dates
for a library book, create a program that calculates the fine (if any). The fee
structure is as follows:
1.If the book is returned on or before the expected return date, no fine will
be charged (i.e.: fine = 0).
2.If the book is returned after the expected return. but still within the same
calendar month and year as the expected return date, fine = Rs.15 * number of
days late.
3.If the book is returned after the expected return month but still within the
same calendar year as the expected return date, the fine = Rs.500 * number of
days late.
4.If the book is returned after the calendar year in which it was expected,
there is a fixed fine of Rs.10,000.
"""
Expected_date=int(input("enter Expected_date :"))
Expected_month=int(input("enter Expected_month  :"))
Expected_year=int(input("enter Expected_year :"))
Return_date=int(input("enter Return_date :"))
Return_month=int(input("enter Return_month  :"))
Return_year=int(input("enter Return_year :"))
if (Expected_date>=Return_date)and (Expected_month == Return_month) and (Expected_year==Return_year):
    print("fine is :",0)
elif Return_date>=Expected_date and ((Expected_month == Return_month) and (Expected_year==Return_year)):
    print("fine is :",(Return_date- Expected_date)*15)
elif ( Return_month >=Expected_month) and (Expected_year==Return_year):
    if Return_date>=Expected_date :
        print("fine is :",(( Return_date-Expected_date)+((Return_month-Expected_month)*30))*500)
    else:
         print("fine is :",(( Return_date-Expected_date)+((Return_month-Expected_month)*30))*500)
elif Return_year>Expected_year:
    print("fine is ",10000)

    