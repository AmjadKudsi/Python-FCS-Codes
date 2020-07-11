#!/usr/bin/env python
# coding: utf-8

# # Grading System

# In[55]:


grade = str
marks = int(input("Enter your marks: "))

if (marks >= 75 and marks <= 100):
    grade = "A"
elif (marks >= 60 and marks < 75):
    grade = "B"
elif (marks >= 45 and marks < 60):
    grade = "C"
elif (marks >= 35 and marks < 45):
    grade = "D"
elif (marks >= 0 and marks < 35):
    grade = "E"
elif (marks < 0):
    grade = "Fail"
else:
    grade = "NA"


if grade == "Fail":
    print("Your grade for marks '", marks, "' is: ",)

    print("\n-*-*-*-*-*-*-*-*")
    print("{              }")
    print("|    ",grade,"    |")
    print("{              }")
    print("-*-*-*-*-*-*-*-*")
    
elif grade == "NA":
    print("Your grade for marks '", marks, "' is: ",)

    print("\n-*-*-*-*-*-")
    print("{         }")
    print("|   ",grade,"  |")
    print("{         }")
    print("-*-*-*-*-*-")
    
else:
    print("Your grade for marks '", marks, "' is: ",)

    print("\n-*-*-*-*-*-")
    print("{         }")
    print("|   ",grade,"   |")
    print("{         }")
    print("-*-*-*-*-*-")
    


# In[ ]:




