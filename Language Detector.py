#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob


# In[14]:


from textblob import TextBlob


a = str(input("Enter atleast word of any language: "))

lang = TextBlob(a)
lang.detect_language()


# In[ ]:




