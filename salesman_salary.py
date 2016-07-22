#! /usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
basic_commision = 0.02
noofcamera = int(input("Enter the number of camera sold : "))
priceofcamera = float(input("price of camera :"))
bonus = (noofcamera * bonus_rate)
commision = (basic_commision * noofcamera * priceofcamera)
print("Bonus         = %6.2f" % bonus)
print("Commision     = %6.2f" % commision)
print("Gross salary  = %6.2f" % (bonus + commision + basic_salary))
