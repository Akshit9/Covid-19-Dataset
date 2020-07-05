#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


corona=pd.read_csv(r'C:\Users\Admin\Downloads\Kaggle Datasets\covid_19_data.csv')
corona.head(10)


# In[3]:


corona.columns


# In[4]:


corona.columns=[x.lower() for x in corona.columns]


# In[5]:


corona.columns


# In[6]:


data_1=corona.pivot_table('confirmed',index='province/state',columns='country/region')


# In[7]:


data_1


# In[8]:


data_2=corona.pivot_table('deaths',index='province/state',columns='country/region')


# In[9]:


data_2


# In[10]:


data_3=corona.pivot_table('recovered',index='province/state',columns='country/region')


# In[11]:


data_3


# In[12]:


confirmed=pd.qcut(corona['confirmed'],4)
corona.pivot_table('deaths',index=['province/state',confirmed],columns='country/region')


# In[13]:


confirmed=pd.qcut(corona['confirmed'],4)
corona.pivot_table('deaths',index=['province/state',confirmed],columns=[confirmed,'country/region'])


# In[14]:


recovered=pd.cut(corona['recovered'],[0,40,90])
corona.pivot_table('deaths',index=['province/state',recovered],columns='country/region')


# In[15]:


corona.pivot_table(index='province/state',columns='country/region',values=['confirmed','recovered'],aggfunc='sum')


# In[16]:


corona.pivot_table(index='province/state',columns='country/region',values=['confirmed','recovered'],aggfunc='sum',margins=True,margins_name='total_sum')


# In[17]:


Data=corona.pivot_table(index='province/state',columns='country/region',values=['confirmed','recovered'],aggfunc='sum',margins=True,margins_name='total_sum').reset_index()


# In[18]:


Data


# In[19]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,8))
d1=plt.plot(corona['confirmed'],color='g')
d2=plt.plot(corona['deaths'],color='r')


# In[20]:


plt.style.use('ggplot')
plt.figure(figsize=(14,12))
d1=plt.plot(corona['confirmed'],'-b',label='confirmed')
d2=plt.plot(corona['deaths'],'-.r',label='deaths')
d3=plt.plot(corona['recovered'],'.g',label='recovered')
plt.legend()


# In[21]:


import seaborn as sns

temp = corona.groupby(['observationdate', 'country/region'])['confirmed'].sum()
temp = temp.reset_index().sort_values(by=['observationdate', 'country/region'])

plt.style.use('seaborn')
g = sns.FacetGrid(temp, col="country/region", hue="country/region", 
                  sharey=False, col_wrap=5)

g = g.map(plt.plot, "observationdate", "confirmed")
g.set_xticklabels(rotation=90)
plt.show()


# In[22]:


import seaborn as sns

temp = corona.groupby(['observationdate', 'country/region'])['confirmed'].sum()
temp = temp.reset_index().sort_values(by=['observationdate', 'country/region'])

plt.style.use('seaborn')
sns.set(style='ticks')
g = sns.FacetGrid(temp, col="country/region", hue="country/region", 
                  sharey=False, col_wrap=5)

g = g.map(plt.plot, "observationdate", "confirmed")
g.set_xticklabels(rotation=90)
plt.show()


# In[23]:


covid_india=corona[corona['country/region']=='India'].reset_index()


# In[24]:


covid_india


# In[25]:


import seaborn as sns

temp = covid_india.groupby(['observationdate', 'province/state'])['confirmed'].sum()
temp = temp.reset_index().sort_values(by=['observationdate', 'province/state'])

plt.style.use('seaborn')
g = sns.FacetGrid(temp, col="province/state", hue="province/state", 
                  sharey=False, col_wrap=5)

g = g.map(plt.plot, "observationdate", "confirmed")
g.set_xticklabels(rotation=90)
plt.show()


# In[26]:


plt.style.use('ggplot')
plt.figure(figsize=(14,12))
d1=plt.plot(covid_india['confirmed'],'-b',label='confirmed')
d2=plt.plot(covid_india['deaths'],'-.r',label='deaths')
d3=plt.plot(covid_india['recovered'],'.g',label='recovered')
plt.legend()


# In[27]:


corona['confirmed'].max()


# In[28]:


covid_india["confirmed"].max()


# In[38]:


import seaborn as sns

covid_19=covid_india.pivot("observationdate","province/state","confirmed")
ax=sns.heatmap(covid_19)


# In[ ]:




