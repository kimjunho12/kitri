# %%
# 대중교통 데이터 분석 (www.t-money.co.kr)

### 2021년 10월 교통카드 통계자료.xls
#### 1. 버스정류장별 이용현황
#### 2. 지하철 노선별 역별 이용현황
#### 3. 지하철 유무임별 이용현황
#### 4. 지하철 시간대별 이용현황
# %%
## 지하철 유무임별 이용현황
#### 1. 사용월 - 날짜형식 : 2021-10 형식으로 사용
#### 2. 작업일시 열은 삭제
#### 3. 숫자데이터 : 천단위 기호 제거 (셀서식 --> 숫자)
# %%
import csv
f = open('./data/교통데이터/2021년 10월  교통카드 통계자료.csv', encoding='utf-8')
data = csv.reader(f)

for i in data:
    print(i)
# %%
import pandas as pd

df = pd.read_csv('./data/교통데이터/2021년 10월  교통카드 통계자료.csv')
# str 형태의 승차 횟수를 int로 변환
for col in df.columns[4:] :
    for i in range(len(df[col])) :
        df[col][i] = int(df[col][i].replace(',',''))

# %%
### 유임승차 비율
#### rate = 유임승차인원/무임승차인원
### 작업순서
#### 1. 데이터 불러오기
#### 2. 각역별 비율 계산
#### 3. 비율이 가장 높은 역을 찾는다

# %%
# 인구 100,000당 비율 계산
mx = 0; mx_idx = 0; rate = 0

for i in range(len(df)) :
    try :
        if (df.iloc[i,6] + df.iloc[i,4] > 100000) : 
            rate = df.iloc[i,4]/(df.iloc[i,6] + df.iloc[i,4])
            if (mx <= rate) :
                mx = rate; mx_idx=i
                mx_station = df.iloc[i,3] + ' ' + df.iloc[i,1]
    except Exception as e:
        print(i, e)
print(mx_idx, round(mx, 2), list(df.loc[mx_idx]))
print(mx_station, round(mx*100, 2))
# %%
# 유무임 승하차가 가장 많은 역
enter_cnt = 0; enter_mx = 0; exit_cnt = 0; exit_mx = 0
for i in range(len(df)) :
    enter_cnt = df.iloc[i,4] + df.iloc[i,6]
    if (enter_mx <= enter_cnt) :
        enter_mx = enter_cnt; enter_mx_idx = i

    exit_cnt = df.iloc[i,5] + df.iloc[i,7]
    if (exit_mx <= exit_cnt) :
        exit_mx = exit_cnt; exit_mx_idx = i

print(enter_mx_idx, enter_mx, list(df.loc[enter_mx_idx]))
print(exit_mx_idx, exit_mx, list(df.loc[exit_mx_idx]))
# %%
# 승하차 가장많은 역 확인 (Pandas / idxmax 활용)
df.iloc[:,4:].astype('int').idxmax()
df.iloc[df.iloc[:,4:].astype('int').idxmax()]

# %%
### 데이터 시각화
from matplotlib import pyplot as plt

label = ['유임승차', '유임하차', '무임승차', '무임하차']
c = ['#123456', '#03A756', '#F2C321', '#BB9234']
plt.rc('font', family='Malgun Gothic')

for i in range(len(df)):    
    plt.figure(dpi=300)
    plt.title(df.iloc[i,1] + ' ' + df.iloc[i,3])
    plt.pie(df.iloc[i,4:], labels= label, colors=c, autopct='%1.f%%')
    plt.axis("equal")
    plt.savefig(f"./data/chart/{df.iloc[i,1]} {df.iloc[i,3]}.png")
# %%
