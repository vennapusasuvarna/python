"""
Q4. Take two user inputs one as day and one as meal time. Show the following
table using nested if statements :
1. Day = Monday
  Breakfast = Poori Sabzi
  Lunch = Sambhar Rice
  Dinner = Chicken Rice
2. Day = Tuesday
◦ Breakfast = Poha
◦ Lunch = Rajma Rice
◦ Dinner = Roti Sabzi.
"""
day=input("enter the day")
meal_time=input("enter the meal_time")
if day=='monday' :
    if meal_time=='breakfast':
        print("Poori Sabzi")
    if meal_time=='lunch':
        print("Sambhar Rice")
    if meal_time=='dinner':
        print("Chicken Rice")
else:
    if day=='tuesday' :
        if meal_time=='breakfast':
            print("Poha")
        if meal_time=='lunch':
            print("Rajma Rice")
        if meal_time=='dinner':
            print("Roti Sabzi")