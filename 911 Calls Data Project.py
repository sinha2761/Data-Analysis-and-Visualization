#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('911.csv')


# In[4]:


df.info()


# In[5]:


df.head()


# In[6]:


#Checking the top 5 zipcodes for 911 calls? 


df['zip'].value_counts().head(5)


# In[7]:


#Checking the top 5 townships (twp) for 911 calls? **

df['twp'].value_counts().head(5)


# In[9]:


df['title'].nunique()


# In[10]:


#Creating a new column Reason.

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[11]:


#The most common Reason for a 911 call

df['Reason'].value_counts()


# In[12]:


#Seaborn to create a countplot of 911 calls by Reason

sns.countplot(x='Reason',data=df,palette='viridis')


# In[13]:


type(df['timeStamp'].iloc[0])


# In[14]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[15]:


#Using .apply() to create 3 new columns called Hour, Month, and Day of Week.

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[16]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[17]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[18]:


#Seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.

sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[19]:


sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[20]:


byMonth = df.groupby('Month').count()
byMonth.head()


# In[21]:


byMonth['twp'].plot()


# In[22]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[23]:


#New column called 'Date' that contains the date from the timeStamp column.

df['Date']=df['timeStamp'].apply(lambda t: t.date())


# In[24]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[25]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[28]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[29]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# In[30]:


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[31]:


#Heat maps with seaborn

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# In[32]:


#Clustermap using this DataFrame.

sns.clustermap(dayHour,cmap='viridis')


# In[33]:


#DataFrame that shows the Month as the column

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[34]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[35]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:




