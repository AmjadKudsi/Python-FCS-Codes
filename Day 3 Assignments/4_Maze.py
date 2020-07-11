#!/usr/bin/env python
# coding: utf-8

# # Maze

# In[2]:


x = 0
y = 0
loop = True

while loop == True:
    coordinates = [x,y]
    print(coordinates)
    
    command = input("Your Command (L/R/U/D): ")

    if(command == 'L'): 
        x -= 1
    if(command == 'R'): 
        x += 1
    if(command == 'U'): 
        y +=  1
    if(command == 'D'): 
        y -=  1
    if(command[0].lower() == 'b'):
        break


# In[ ]:




