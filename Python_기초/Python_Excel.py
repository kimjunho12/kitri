# %%
import sys
from glob import glob
import pandas as pd

# 딕셔너리 선언
excel_exam_data1 = {
    '학생': ['최원석', '류건혁', '최난', '유혜미', '정현우'],
    '국어': [100] * 5,
    '영어': [90] * 5,
    '수학': [80] * 5,
    '과학': [70] * 5
}
# %% 데이터 객체 생성
df = pd.DataFrame(excel_exam_data1,)
df.to_excel('./data/학생시험성적2.xlsx', encoding='utf-8', index=False)
# %%
# 판다스의 자료형
# - 시리즈(Series) : 1차원 데이터 --> 행 또는 열이 1개뿐인 데이터
# - 데이터프레임(Dataframe) : 다차원 데이터
# %%
excel_writer = pd.ExcelWriter('./data/학생시험성적.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, index=False)
excel_writer.save()
# %%
excel_exam_data2 = {
    '학생': ['A', 'B', 'C', 'D', 'E'],
    '한식': [100, 60, 70, 80, 60],
    '중식': [70, 80, 60, 90, 100],
    '일식': [80, 90, 100, 70, 90],
    '양식': [70, 100, 90, 80, 80],
}
df2 = pd.DataFrame(excel_exam_data2)
df2.to_excel('./data/학생요리성적.xlsx', encoding='utf-8', index=False)
# %%
# 데이터 저장 옵션
# 기본 옵션 : sheet_name = 0 / index_col = 0

# %%
# 1개의 excel 파일에 2개의 데이터를 각각 다른 시트에 저장
with pd.ExcelWriter('./data/학생시험성적3.xlsx', engine='xlsxwriter') as w:
    df.to_excel(w, sheet_name='일반교과목', index=False)
    df2.to_excel(w, sheet_name='교양교과목', index=False)

# %%
# 엑셀파일 합치기
excel_data_files = [
    './data/예제_데이터/담당자별_판매량_Andy사원.xlsx',
    './data/예제_데이터/담당자별_판매량_Becky사원.xlsx',
    './data/예제_데이터/담당자별_판매량_Chris사원.xlsx'
]
# %%
total_data = pd.DataFrame()
for i in excel_data_files:
    total_data = total_data.append(pd.read_excel(i), ignore_index=True)
# %%
# 실습 100개의 excel 파일 통합

excel_data_files2 = glob('./data/예제_데이터/담당자*')
total_data2 = pd.DataFrame()
for i in excel_data_files2:
    total_data2 = total_data2.append(pd.read_excel(i), ignore_index=True)
total_data2.to_excel('./data/담당자_판매량통합.xlsx', index=False, sheet_name='판매량통합')
# %%
# 파일들의 위치가 다를때 파일 통합
import sys
from glob import glob

input_files = sys.argv[1]       # 파일이 있는 경로와 파일명 python 실행시 입력 parameter
output_filename = sys.argv[2]   # 저장할 통합 파일이름
output_sheetname = sys.argv[3]  # 저장할 파일의 시트 이름

excel_data_files2 = glob(input_files)
total_data2 = pd.DataFrame()
for i in excel_data_files2:
    total_data2 = total_data2.append(pd.read_excel(i), ignore_index=True)
total_data2.to_excel(output_filename, index=False, sheet_name=output_sheetname)

# %%
df = pd.read_excel('./data/예제_데이터/담당자별_판매량_Andy사원.xlsx')
df1 = df[['제품명', '1분기', '2분기', '3분기', '4분기']]
# %%
df1.loc[2, '4분기'] = 500
df1
# %%
df1.iloc[1,3] = 750
df1
# %%
df.loc[3, '제품명'] = '운동화'
df.loc[3, '담당자'] = 'A'
df.loc[3, '지역'] = '가'
df.loc[3, '1분기'] = 100.0
df.loc[3, '2분기'] = 200.0
df.loc[3, '3분기'] = 300.0
df.loc[3, '4분기'] = 400.0
# %%
df['지역'].replace('가', '구로구', inplace=True)
df
# %%
excel_file_name = "./data/예제_데이터/담당자별_판매량_Andy사원10.xlsx"
df.to_excel(excel_file_name, index=False)
glob(excel_file_name)   # 파일 생성 확인
# %%
