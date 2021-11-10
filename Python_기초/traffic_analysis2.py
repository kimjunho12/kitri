# %%
## 지하철 시간대별 데이터 분석
#### 1. 출근 시간대 가장 많이 타고 내린 역은?
#### 2. 시간대별로 가장 많이 타고 내린 역은?
# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/교통데이터/2021년 10월  교통카드 시간별 통계자료.csv', encoding='cp949')
df
# # %%
# ### zip 함수
# list(zip([1,2,3], [4,5,6]))
# %%
for i in range(1, len(df)) :
    df.iloc[i,4:] = df.iloc[i,4:].map(lambda x : int(x.replace(',','')))
# %%
### 오전 7시의 승차데이터
result = []

for i in range(1, len(df)) :
    result.append(df.iloc[i,10]) # 오전 7시의 승차 데이터만 추출

# %%
### 데이터 시각화
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()
# %%
### 그래프를 오름차순으로 정렬하여 시각화
result.sort()
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()
# %%
### 오전 7~9시까지의 승차인원이 많은 역
df_ent79 = df.iloc[1:, 10] + df.iloc[1:, 12]
df.iloc[df_ent79.astype('int').idxmax(), :4]
# %%
### 오전 7~9시까지의 하차인원이 많은 역
df_ex79 = df.iloc[1:, 11] + df.iloc[1:, 13] + df.iloc[1:, 15]
df.iloc[df_ex79.astype('int').idxmax(), :4]
# %%
### 저녁 11시에 승차인원이 가장 많은역
df.iloc[df.iloc[1:, 42].astype('int').idxmax(), [1,3]]
# %%
df.iloc[df.iloc[1:, 42].astype('int').sort_values(ascending=False).index[:5], [1,3, 42]]
# %%
t = int(input('어느 시간대의 승차인원을 검색할까요?> '))
df.iloc[df.iloc[1:, t*2-4].astype('int').sort_values(ascending=False).index[:5], [1,3, t*2-4]]
# %%
# %%
### 시간대 별로 승하차 인원이 가장 많은역
for t in range(4, len(df.columns), 2) :
    print('승차 :', df.columns[t], list(df.iloc[df.iloc[1:, t].astype('int').idxmax(), [1,3, t]]))    # 승차
    print('하차 :', df.columns[t], list(df.iloc[df.iloc[1:, t+1].astype('int').idxmax(), [1,3, t+1]]))  # 하차
# %%
