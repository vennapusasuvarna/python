"""32. Write a program to calculate the electricity bill (accept number of unit from user) according to the
following criteria :
Unit                 Price
First 100 units    no charge
Next 100 units     Rs 5 per unit
After 200 units    Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)"""
units=int(input("enter the no of units     :"))
if units<=100 :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    bill=units*0
if units>100  and units<=200 :
    bill=(units-100)*5
if units>200 :
    bill=(100*5)+(units-200)*10
print(bill)


