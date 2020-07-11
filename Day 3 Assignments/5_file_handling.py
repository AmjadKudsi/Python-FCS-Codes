#!/usr/bin/env python
# coding: utf-8

# In[2]:


file = open("FCS.txt", 'w')
file.write("I love FCS")
file.close()

file = open("FCS.txt",'r')
text = file.read()
print(text)


# In[ ]:




