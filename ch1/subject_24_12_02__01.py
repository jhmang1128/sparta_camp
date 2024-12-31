import random

correct_answer = random.randint(1, 10)
print("1~10 사이의 숫자를 맞춰보세요")

while True:
    player_answer = int(input("입력 : "))
    if player_answer == correct_answer:
        print(f" {correct_answer} 정답 입니다!")
        exit()
    else:
        print("오답입니다.")