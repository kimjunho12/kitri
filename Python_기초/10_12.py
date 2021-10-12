# 파이선 기본
# %%
# 예약어 확인
import keyword
print(keyword.kwlist)
# %%
# 이름, 나이를 입력 받아 몇년생인지 출력한다.
name, age = input("이름과 나이를 입력 해 주세요. : ").split(); age = int(age)
print(f"{name}은 {2021-age+1}년생입니다.")
# %%
# pprint() 함수 사용 : Pretty Print()   복잡한 데이터 깔끔한 출력 결과
complicated = ['spam', (1,2,3), ('ham', 'egg', ('ab','cd',('abc','def')))]
complicated *= 3
print(complicated, end='\n'+'-'*80+'\n')

import pprint
pprint.pprint(complicated)
# %%
# BMI 계산 프로그램
height = int(input('키를 입력 해 주세요. : '))
weight = float(input('몸무게를 입력 해 주세요. : '))
print(f"키는 {height}, 몸무게는 {weight}입니다.")
print("BMI 지수는 %.2f입니다."% (weight/(height/100)**2))
# %%
num1 = input("첫번째 숫자 입력 : ")
num2 = input("두번째 숫자 입력 : ")

print('num1 : ', num1)
print('num2 : ', num2, end='\n'+'-'*80+'\n')

tmp = num1
num1 = num2
num2 = tmp
del tmp

print('num1 : ', num1)
print('num2 : ', num2, end='\n'+'-'*80+'\n')

num1, num2 = num2, num1


print('num1 : ', num1)
print('num2 : ', num2)

# %%
