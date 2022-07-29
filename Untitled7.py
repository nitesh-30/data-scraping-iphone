#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[35]:


import pandas as pd


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup as bs


# In[4]:


import requests


# In[30]:


content=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content
data = bs(content.content,"html.parser")
price=[]
dis=[]
img=[]
pri=data.find_all('div',class_="_30jeq3 _1_WHN1")
for i in pri:
    price.append(i.text)
disc=data.find_all('div',class_="_4rR01T")
for i in disc:
    dis.append(i.text)
im=data.find_all('img', class_="_396cs4 _3exPp9")
for p in im:
    img.append(p.get('src'))

    


    


# In[43]:


len(img)


# In[42]:


img=img[0:24]


# In[46]:


df={"iphone-name":dis,'Price':price,'image':img}


# In[47]:


new=pd.DataFrame.from_dict(df)


# In[48]:


new


# In[24]:


content=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content
data = bs(content.content,"html.parser")
data.find('span')

