class person:
    # person 객체 생성 시 변수 초기화
    def __init__(self):
        self.name = input("이름 입력 : ")
        self.gender = input("성별 입력 : ")
        if not (self.gender == "male" or self.gender == "female"):
            print("잘못된 성별을 입력하셨습니다."), exit()
        self.age = int(input("나이 입력 : "))
        
    # 이름 성별 나이 print
    def display(self):
        print(self.name, self.gender)
        print(self.age)
        
    # display의 기능 + 나이대에 맞는 인삿말 출력
    def greet(self):
        print(self.name, self.gender)
        print(self.age)
        
        if 0 < self.age < 20: print("안녕하세요 미성년자시군요!")
        elif 20 <= self.age: print("안녕하세요 성인이시군요!")
        

# 객체 생성할지 사용자에게 확인
print("사람 객체를 생성하시겠습니까?")
input_person = input("y or n :")

if input_person == "y":
    # 사람 객체 생성
    person_01 = person()
    print("사람 객체가 생성 되었습니다.")
    
    # display 실행
    print("\n\n***************************************************************")
    print("- display")
    person.display(person_01)
    
    # greet 실행
    print("- greet")
    person.greet(person_01)
    
elif input_person == "n":
    print("프로그램을 종료합니다.")
    exit()
else:
    print("잘못된 문자를 입력하셨습니다.")