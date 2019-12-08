# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:06:36 2019

@author: reddy
"""

print("This is a practice workbook for code learned so far")

#First we begin by doing basic math 

my_age = 41
my_first_name = "vikram"
my_last_name = "reddy"

my_monthly_brokerage = 150000
my_broker_cut = 0.60
my_tax_rate = 0.50

annual_growth_rate = 1.075

annual_earnings = my_monthly_brokerage*my_broker_cut*my_tax_rate*12

full_name = my_first_name + " " + my_last_name 

print(full_name.title() + "'s" + " " + "Annual Earnings are" + " " 
      + str(annual_earnings))

print("The annual earnings of {}".format(full_name.title()) +
      " " "is" + " " +str(annual_earnings))

#another way to do this is to use float formatting like below

print("The annual earnings of {}".format(full_name.title()) +
      " " "is" + " " +"{a:1.0f}".format(a=annual_earnings))

