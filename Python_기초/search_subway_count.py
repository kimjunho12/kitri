import pandas as pd

df = pd.read_csv('./data/교통데이터/2021년 10월  교통카드 시간별 통계자료.csv', encoding='cp949')
for i in range(1, len(df)) :
    df.iloc[i,4:] = df.iloc[i,4:].map(lambda x : int(x.replace(',','')))
t = int(input('어느 시간대의 승차인원을 검색할까요?> '))
df.iloc[df.iloc[1:, t*2-4].astype('int').sort_values(ascending=False).index[:5], [1,3, t*2-4]]

input('Press Any Key to Exit......')