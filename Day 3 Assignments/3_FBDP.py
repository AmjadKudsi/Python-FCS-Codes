#!/usr/bin/env python
# coding: utf-8

# # Facebook Dp update

# In[ ]:


loop = True
while loop == True:
    L = int(input("Enter the side length of profile pic: "))
    if L<1:
        print("Too small! Try again")
        break

    elif L> 10000:
        print("Too large! Try again")
        break

    N = int(input("Enter number of photos available in your memory: "))
    if N<1:
            print("Memory is empty!")
            break
    
    elif N> 1000:
            print("Too many!")
            break
            
    for i in range(1,N):
        wh = (input().split())
        w = int(wh[0])
        h = int(wh[1])
        
        if (w<1 or h<1):
            print("Too small! Try again")
            break
        elif (w>10000 or h>10000):
            print("Too large! Try again")
            break
            
        elif (w < l or h < l):
            print('UPLOAD ANOTHER')

        else:
            if(w == h): 
                print('ACCEPTED')
                
            elif(w>h or w<h):
                print('CROP IT')


# In[ ]:




