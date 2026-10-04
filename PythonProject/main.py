
principle = float(input("enter principle amount:"))
while principle <=0:
 print("principle can't be less than or equal to zero")
 principle = float(input("enter principle amount:"))

 print(f"your principle amount is{principle} dollars")

rate = float(input("enter rate of interest:"))
while rate < 0:
     print("rate can't be less than or equal to zero")
     rate = float(input("enter rate of interest :"))

     print(f"your principle amount is {rate} %")

time = float(input("enter years(months/years):"))
while time <= 0:
    print("time can't be less than or equal to zero")
    time = float(input("enter time:"))

    print(f"Time period is:{time} years")

interest = principle * (rate/100) * (time * 12)
print(f"the total interest is: {interest}")

total = interest + principle
print(f"the total amount can be returned is: {total}")





