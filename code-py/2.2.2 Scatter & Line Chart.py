#!/usr/bin/env python
# coding: utf-8

# # Scatter & Line Chart

# ## Scatter Chart 기본 구문

# In[ ]:


trace = go.Scatter(x = 수치형 값,
                   y = 수치형 값,
                   mode = 'markers',
                   marker = dict(size = 크기 값)
                   )
data = [ trace ]
layout = go.Layout(디자인 옵션)
fig = go.Figure(data, layout)
fig.show()


# - https://plotly.com/python/line-and-scatter/

# |Chart 구분|옵션|내용|  
# |:-----:|:---:|:---:| 
# |Line|mode = 'lines'|선|  
# |Scatter|mode = 'markers'|점|  
# |Scatter & Line|mode = 'markers + lines'|점 + 선|  

# ## 반복문 구조

# In[ ]:


# 반복문을 통한 그래프 중첩
traces = []  # 빈 리스트 생성
for 참조값 in 참조리스트 :
    traces.append(df[df['참조변수' == 참조값 ]])


# In[1]:


import numpy as np
import pandas as pd

import plotly.graph_objects as go


# In[2]:


# 데이터 호출
df = pd.read_csv('data/Sales data/Data.csv')


# In[3]:


df.head(3)


# In[4]:


# 연도, 월 변수 생성
df['year'] = df['OrderDate'].str.slice(start = 0, stop = 4)
df['month'] = df['OrderDate'].str.slice(start = 5, stop = 7)

# 데이터 정렬
df = df.sort_values(by = ['Region','Channel','Category','Item Type','year','month','Gender'])


# In[5]:


df.info()


# In[6]:


# 연도별 월 매출 현황 비교 - 연/월별 매출 합계 산출
df_g = df.loc[:,['Revenue','year','month']].groupby(by = ['year','month'], as_index = False).sum()


# In[7]:


# 연도 오름차순 정렬
year = list(df_g['year'].unique())
year.sort()
year


# In[8]:


df_g.head()


# ## 기본 그래프

# In[9]:


df_g20 = df_g[df_g['year'] == '2020']
trace = go.Scatter(x = df_g20['month'],
                   y = df_g20['Revenue'],
                   mode = 'lines+markers',
                   marker = dict(size = 10),
                  )
data = [trace]
layout = go.Layout(title = 'Chapter 2.2 - Scatter & Line Charts',
                   xaxis = dict(title = 'Month'),
                   yaxis = dict(title = 'Revenue'))
fig = go.Figure(data, layout)
fig.show()


# ![image.png](attachment:image.png)

# ## 연도별 월 매출액 비교 - 중첩 Scatter & Line Chart 구현

# In[10]:


traces = []
for years in year:
    tmp = df_g[df_g['year'] == years]
    traces.append(go.Scatter(x = tmp['month'],
                             y = tmp['Revenue'],
                             mode = 'lines+markers',
                             marker = dict(size = 10),
                             name = years
                           ))
data = traces
layout = go.Layout(title = 'Chapter 2.2 - Scatter & Line Charts',
                   xaxis = dict(title = 'Month'),
                   yaxis = dict(title = 'Revenue'))
fig = go.Figure(data, layout)
fig.show()


# ![image.png](attachment:image.png)
