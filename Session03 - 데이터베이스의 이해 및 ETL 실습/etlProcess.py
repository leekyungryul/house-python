#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# In[ ]:





# ### 데이터 불러오기

# In[3]:


indata =     pd.read_csv("../dataset/kopo_decision_tree_all_new.csv")


# In[5]:


indata.shape
# 컬럼과 행 정보를 표시


# ### 3. 데이터 처리(컬럼 소문자로 변환)

# In[7]:


indata.columns


# In[11]:


indata.columns = indata.columns.str.lower()
indata.columns
# 소문자로 변환한다.


# In[ ]:





# In[18]:


targetDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopo"
targetDbPrefix = "postgersql://"


# In[19]:


targetUrl = "{}{}:{}@{}/{}".format(targetDbPrefix,
                                   targetDbId,
                                   targetDbPw,
                                   targetDbIp,
                                   targetDbPort,
                                   targetDbName)


# In[20]:


engine_pg = create_engine(targetUrl)


# In[14]:


tableName = "pgout_kopo_hk"


# In[ ]:


indata.to_sql(name = tableName,
             con =  )

