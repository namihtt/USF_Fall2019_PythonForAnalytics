#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Loading data into Python
import pandas as pd #import pandas library
df = pd.read_csv('ThaiLiveSell.csv') #read data


#Cleaning data
df.drop_duplicates(inplace=True) #drop duplicates if any
df['status_published'] = pd.to_datetime(df['status_published']) #change data type of status_published to make it look nicer


#Creating new attributes to have a more specific analysis

#extracting specific information out of the status_published column
df['year'] = df['status_published'].dt.year
df['month'] = df['status_published'].dt.month
df['day'] = df['status_published'].dt.day
df['dayofweek'] = df['status_published'].dt.dayofweek #0 is Monday, 6 is Sunday.
df['hour'] = df['status_published'].dt.hour

#ranking columns
df['reactionranked'] = df['num_reactions'].rank(ascending=1)
df['sharesranked'] = df['num_shares'].rank(ascending=1)

#converting string categories to numerical variables
def type_to_numeric(x): #define the function to convert approriate values into numerical values
    if x=='link':
        return 1
    if x=='photo':
        return 2
    if x=='status':
        return 3
    if x=='video':
        return 4
df['status_type_val'] = df['status_type'].apply(type_to_numeric) #converting values


#Organizing data: drop columns that are not useful for the analysis
df.drop('status_id', axis=1, inplace=True) 
df.drop('num_comments', axis=1, inplace = True)
df.drop('num_likes', axis=1, inplace = True)
df.drop('num_loves', axis=1, inplace = True)
df.drop('num_wows', axis=1, inplace = True)
df.drop('num_hahas', axis=1, inplace = True)
df.drop('num_sads', axis=1, inplace = True)
df.drop('num_angrys', axis=1, inplace = True)

df.shape


# In[8]:


df


# In[ ]:




