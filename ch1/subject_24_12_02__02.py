class person:
    def __init__(self):
        self.name = input("이름 입력 : ")
        self.gender = input("성별 입력 : ")
        self.age = input("나이 입력 : ")
    def display(self):
        print(self.name, self.gender)
        print(self.age)
        

print("사람 객체를 생성하시겠습니까?")
input_person = input("y or n :")

if input_person == "y":
    person_01 = person()
    print("사람 객체가 생성 되었습니다.")
    person.display(person_01)
elif input_person == "n":
    print("프로그램을 종료합니다.")
    exit()
else:
    print("잘못된 문자를 입력하셨습니다.")