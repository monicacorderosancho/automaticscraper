#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


##We can read the content of the server’s response.
response = requests.get('https://www.whitehouse.gov/briefing-room/')
doc = BeautifulSoup(response.text,'html.parser')


# In[8]:


# How many pages there are to scrape

[item.text for item in doc.select(".page-numbers")]


# In[13]:


# list of number of pages diplayed on the homepage
number_of_pages = [int(item.text.strip('Page ')) for item in doc.select('.page-numbers a')]


# In[14]:


# get the biggest number
max_num_of_pages = max(number_of_pages)


# In[15]:


# List of numbers from 1 to the max_num_of_pages
list_with_pages = list(range(1, max_num_of_pages+1))


# In[16]:


# List of urls with all the pages to scrape
page_urls = []
for page in list_with_pages:
    url = f"https://www.whitehouse.gov/briefing-room/page/{page}/"
    page_urls.append(url)


# In[17]:


all_pages = []
for page in page_urls:
    response = requests.get(page)
    doc = BeautifulSoup(response.text,'html.parser')
    all_articles = doc.find_all('article') 
    for article in all_articles:
        d = {}
        title = article.find('a').text.strip()
        #print (title)
        article_url = article.find('a')['href']
        #print(article_url)
        article_date = article.find('time').text.strip()
        #print(article_date)
        d['title'] = title
        d['url'] = article_url
        d['article_date'] =  article_date
        all_pages.append(d)
        


# In[18]:


pd.DataFrame(all_pages)


# In[ ]:


#


# In[ ]:


## all_articles = doc.find_all('article')
## df = pd.DataFrame()
## for article in all_articles:
    ##title = article.find('a').text.strip()
    ##print (title)
    ##article_url = article.find('a')['href']
    ##print(article_url)
    ##article_date = article.find('time').text.strip()
    ##print(article_date)
    ##d = {}
    ##print(title)
    ##print(article_url)
    ##print(article_date) 
    ##d['title'] = title
    ##d['url'] = article_url
    ##d['article_date'] =  article_date
    ##df = df.append(d,ignore_index=True)
    
##print(df)
    

