#!/usr/bin/env python
# coding: utf-8

# # Bar Chart

# ## Bar Chart 기본 구문

# In[ ]:


trace = go.Bar(x = 범줒형 값, y = 수치형 값)

data = [trace]
layout = go.Layout(디자인 옵션)
fig = go.Figure(data, layout)
fig.show()


# - https://plotly.com/python/bar-charts/

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
df['year'] = df['OrderDate'].str.slice(start = 0, stop =4)
df['month'] = df['OrderDate'].str.slice(start = 5, stop =6)

# 데이터 정렬
df = df.sort_values(by = ['Region', 'Channel','Category','Item Type','year','month','Gender'])


# In[5]:


df.info()


# - data['변수'].str.slice(start = 시작위치, stop=종료위치)  
#     - 변수에서 일부 값을 추출  
#   
# 
# - df.sort_values(by=['변수1', '변수2'])  
#     - 데이터에서 기준 변수로 정렬을 시켜줍니다.  
#     - '변수1'에 대해 정렬한 뒤, '변수2'에 대해 정렬
# 
# 
# - df.info()  
#     - 데이터의 전체적인 구조를 파악

# In[6]:


# 202년 이익 변수 생성
d20 = df[df['year'] == '2020'].copy()
d20['Margin'] = d20['Revenue'] - d20['Cost']


# In[7]:


# Country별 매출 및 이익 합계 산출
df_g = d20.loc[:, ['Country','Revenue','Margin']].groupby(by=['Country'], as_index =False).sum()
df_g = df_g.sort_values(by = ['Revenue'], ascending = False)


# In[8]:


# 매출 순위 변수 (rank) 생성 후, 매출 사위 1개 Country 추출
df_g['rank'] = list(range(1, len(df_g['Country'])+1))
df_g1 = df_g[df_g['rank'] <= 10].reset_index(drop=True)
df_g1


# - df.groupby(by=['변수'], as_index=False).sum()  
#     - 데이터에서 특병 변수를 그룹화하여 합계를 계산
#     - 코드 끝 부분에 따라 구할 수 있는 통계량은 다양함
#     
#     
# |구분|합계|평균|분산|분산|최댓값|최솟값|
# |-----|---|---|---|---|-----|-----|
# |명령어|.sum()|.mean()|.var()|.std()|.max()|.min()|
# 

# ## 국가별 매출액 - Bar Chart 구현

# In[9]:


trace = go.Bar(
    x = df_g1['Country'],
    y = df_g1['Revenue'],
    text = round(df_g1['Revenue'], 2),
    textposition='none')
data = [trace]
layout = go.Layout(title='Chapter 2.1 - Bar Chart')
fig = go.Figure(data, layout)
fig.show()


# ![image-2.png](attachment:image-2.png)

# ## 국가별 매출액 대비 이익액 - 중첩 Bar Chart 구현

# In[10]:


trace1 = go.Bar(
    y = df_g1['Country'],
    x = df_g1['Revenue'],
    name = 'Revenues',
    orientation = 'h')
trace2 = go.Bar(
    y = df_g1['Country'],
    x = df_g1['Margin'],
    name = 'Margins',
    orientation = 'h')
data = [trace1, trace2]
layout = go.Layout(title = 'Chapter 2.1 - Bar Chart', 
                   barmode = 'group',
                   yaxis = dict(autorange='reversed')
                  )
fig = go.Figure(data, layout)
fig.show()


# ![image.png](attachment:image.png)
