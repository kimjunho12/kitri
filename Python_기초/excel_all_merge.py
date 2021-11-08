import sys
import pandas as pd
from glob import glob

input_files = sys.argv[1]       # 파일이 있는 경로와 파일명
output_filename = sys.argv[2]   # 저장할 통합 파일이름
output_sheetname = sys.argv[3]  # 저장할 파일의 시트 이름

excel_data_files2 = glob(input_files)
total_data2 = pd.DataFrame()
for i in excel_data_files2:
    total_data2 = total_data2.append(pd.read_excel(i), ignore_index=True)
total_data2.to_excel(output_filename, index=False, sheet_name=output_sheetname)
