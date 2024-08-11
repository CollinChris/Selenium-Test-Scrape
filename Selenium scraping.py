#!/usr/bin/env python
# coding: utf-8

# In[81]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.add_experimental_option("detach", True)


# In[82]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# In[83]:


def login():
    url = 'https://www.campbells.com.au/convenience'
    user = '0032353419'
    password = 'Australia@1'
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'loginLink').click()
    time.sleep(1)
    driver.find_element(By.ID, 'j_username').send_keys(user)
    time.sleep(1)
    driver.find_element(By.ID, 'j_password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'loginButton').click()


# In[84]:


login()


# In[85]:


driver.get('https://www.campbells.com.au/convenience/foodservice/general-merchandise/party-&-giftware?pageSize=100&q=%3Arelevance#')
time.sleep(10)


# In[88]:


html = driver.page_source


# In[ ]:


soup = BeautifulSoup(html, 'html.parser')


# In[91]:


products = soup.find_all("div", {"class":"productListItemLeft"})


# In[ ]:





# In[ ]:





# In[ ]:





# In[73]:





# In[74]:





# In[ ]:





# In[12]:





# In[13]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




