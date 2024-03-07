import os
import faker
import pandas as pd

# 디렉토리 생성
directory = 'D:/port/work-1/work/파이썬연습2월/12-1.가짜 개인정보를 만들어 엑셀에 저장하기'
os.makedirs(directory, exist_ok=True)

# Faker 라이브러리의 인스턴스 생성
fake = faker.Faker()

# 가짜 정보를 담을 리스트 생성
fake_data = []

# 1000개의 가짜 정보 생성 및 리스트에 추가
for _ in range(1000):
    fake_name = fake.name()
    fake_gender = fake.random_element(elements=('Male', 'Female'))
    fake_email = fake.email()
    fake_phone_number = fake.phone_number()
    fake_data.append([fake_name, fake_gender, fake_email, fake_phone_number])

# 데이터프레임 생성
df = pd.DataFrame(fake_data, columns=['Name', 'Gender', 'Email', 'Phone Number'])

# 엑셀 파일로 저장
file_path = os.path.join(directory, '개인정보.xlsx')
df.to_excel(file_path, index=False)

print("엑셀 파일이 성공적으로 생성되었습니다.")