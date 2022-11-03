#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data=pd.read_csv('C:/Users/Rakesh/Datasets/unemployment.csv')


# In[3]:


data.head()


# In[4]:


data.columns=['States','Date','Frequency','Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate','Region','longitude','latitude']


# In[5]:


data.head()


# In[6]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
sns.heatmap(data.corr())
plt.show()


# In[8]:


data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region",
               "longitude","latitude"]
plt.title('Indian Unemployment')
sns.histplot(x='Estimated Employed', hue='Region', data=data)
plt.show()


# In[9]:


plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()


# ## Dashboard to analyze the unemployment rate of each Indian state by region

# In[10]:


unemployment=data[['States','Region','Estimated Unemployment Rate']]
figure=px.sunburst(unemployment,path=['Region','States'], values='Estimated Unemployment Rate', width=700, height=700, color_continuous_scale='RdY1Gn',title='Unemployment Rate In India')
figure.show()

