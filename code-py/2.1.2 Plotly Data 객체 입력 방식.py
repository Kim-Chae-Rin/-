#!/usr/bin/env python
# coding: utf-8

# # Plotly Data 객체 입력 방식

# ### 방법 1. add_trace( ) 함수 사용
# - 맨 처음 fig를 정의하고 그 후에 데이터를 추가
# - 그래프를 중첩하여 그리고 싶다면 add_trace()를 연속으로 사용
# - update_layout()을 사용하여 디자인 변경
# ```python
# fig = go.Figure()
# fig.add_trace(go.Bar())
# fig.add_trace(go.Bar())
# fig.show()
# ```
# 
# ### 방법 2. Figure( ) 함수 사용 - 1
# - Figure()에 직접적으로 data객체를 정의하여 넣어주는 방법
# - go.Figure(data = []) 형식
# - 반드시 data 객체를 대괄호 []로 묶어줘야 한다
# - 그래프를 중첩의 경우에는 data = [ trace1, trace2 ]와 같이 리스트 형식으로 묶어줌
# ```python
# fig = go.Figure(
#     data = [go.Bar(), go.Bar()]
# )
# fig.show()
# ```
# 
# ### 방법 3. Figure( ) 함수 사용 - 2
# - data객체를 사전에 정의한 뒤, 마지막에 Figure()에 넣어주는 방법
# ```python
# trace1 = go.Bar()
# trace2 = go.Bar()
# data = [trace1, trace2]
# fig = go.Figure(data)
# fig.show()
# ```

# ## Plotly 시각화 기본 구문

# In[ ]:


import plotly.graph_objects as go
trace = go.Chart()
data = [trace]
layout = go.Layout()
fig = go.Figure(data, layout)
fig.show()


# - go.Chart() : go.Bar(), go.Scatter 등과 같은 Chart 종류를 입력
