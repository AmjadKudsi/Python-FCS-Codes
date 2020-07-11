#!/usr/bin/env python
# coding: utf-8

# # Guess the score!

# In[30]:


import random

score = random.randint(1,250)
lowlimit = score - 10
highlimit = score + 10

guess = int(input("Enter your guess for Indian team score in upcoming T20 match : "))

print("The score is: ",score)

if (guess < 1 or guess > 250):
    print("Reduce your expectation for 20-20 Cricket!")
    
elif (guess >= lowlimit and guess <= highlimit):
    print("Close By, You are a True Indian fan!")
    
else:
    print("You are not a true Indian Fan! :P")


# In[ ]:




