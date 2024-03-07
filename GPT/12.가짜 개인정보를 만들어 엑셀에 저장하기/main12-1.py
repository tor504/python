import random
import faker

# faker 라이브러리의 인스턴스 생성
fake = faker.Faker()

# 가짜 이름 생성
fake_name = fake.name()

# 가짜 이메일 주소 생성
fake_email = fake.email()

# 가짜 주소 생성
fake_address = fake.address()

# 가짜 전화번호 생성
fake_phone_number = fake.phone_number()

print("가짜 이름:", fake_name)
print("가짜 이메일:", fake_email)
print("가짜 주소:", fake_address)
print("가짜 전화번호:", fake_phone_number)