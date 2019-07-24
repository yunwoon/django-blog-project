from faker import Faker #faker는 클래스, 가짜 데이터를 생성할 수 있는 클래스!

myfake = Faker() #가짜 데이터 생성할 수 있는 객체 생성
# 한글버전 myfake = Faker('ko_KR')

#Faker의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼지 결정
#seed 파일 <- 코드를 실행할때마다 같은 faker 파일이 도출 (seed 번호에 저장)
myfake.seed() #괄호 안에 1 넣으면 1번 가짜 데이터 되는 거야

print(myfake.name()) #가짜 이름 생성
print(myfake.address()) #가짜 주소 생성
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())
