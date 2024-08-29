#!/usr/bin/env python
# coding: utf-8

# In[5]:


def remove_duplicates(my_list):
    return [x for i, x in enumerate(my_list) if x not in my_list[:i]]
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("Original list:", my_list)
print("List with duplicates removed:", remove_duplicates(my_list))


# In[ ]:




