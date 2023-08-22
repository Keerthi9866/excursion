#!/usr/bin/env python
# coding: utf-8

# # Level 1 Tasks

# # String Reversal

# In[14]:


def reverse(str):
    return str[::-1]

str=input("Enter an string: ")
print("Reverse of a string: ",reverse(str))


# # Temperature Conversion

# In[15]:


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice='y'
while(choice=='y'):
    print("Temperature Conversion")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsiuis")

    option=int(input("Select an option: "))

    if option==1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    elif option == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")
    choice = input("Do you want to perform another calculation? (y/n): ").lower()


# # Email Validator
# 

# In[16]:


import re

def is_valid_email(email):
    # Regular expression pattern for a basic email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Test the function
email = input("Enter an email address: ")
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")


# # Calculator Program

# In[17]:


def Addition(num1,num2):
    return num1+num2
def Subtraction(num1,num2):
    return num1-num2
def Multiplication(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num1/num2
def Percentage(num1,num2):
    return num1%num2

choice='y'
while(choice=='y'):
    print("Simple Calculator Operations:")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Percentage")
    
    option=int(input("Select an option:"))
               
    if option == 1:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        print("Addition of", num1, "and", num2, "is:", Addition(num1, num2))
    elif option == 2:  
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        print("Subtraction of", num1, "and", num2, "is:", Subtraction(num1, num2))
    elif option == 3:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        print("Multiplication of", num1, "and", num2, "is:", Multiplication(num1, num2))
    elif option == 4:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        print("Division of", num1, "by", num2, "is:", Division(num1, num2))
    elif option == 5:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        print("Percentage of", num1, "divided by", num2, "is:", Percentage(num1, num2))
    else:
        print("Invalid option. Please select a valid operation.")

    choice = input("Do you want to perform another calculation? (y/n): ").lower()


# # Palindrome Checker

# In[18]:


def palindrome(str):
    flag=False
    if str.lower()==str[::-1].lower():
        flag=True
    return flag

str=input("Enter an string: ")
result=palindrome(str)

if result==True:
    print(str," is palindrome")
else:
    print(str," is not palindrome")


# In[ ]:




