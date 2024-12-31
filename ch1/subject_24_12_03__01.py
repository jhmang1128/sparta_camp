import random

# 정답 생성
while True:
    correct_answer = random.randint(1, 10)
    print("1~10 사이의 숫자를 맞춰보세요")


    while True:
        # 플레이어의 답변이 숫자형인지 확인
        try: player_answer = int(input("입력 : "))
        except :
            print("정수를 입력해주세요")
            break
        type_pa = type(player_answer)
        
        # 정해진 숫자 범위를 벗어날 때
        if not (1 <= player_answer <= 10):
            print("1~10 사이의 숫자를 입력해주세요")
            
        
        # 정답 확인
        if player_answer == correct_answer:
            print(f" {correct_answer} 정답 입니다!")
            break
        else:
            print("오답입니다.")
            
    # 게임 재시작 여부 확인
    restart_value = input("게임 재시작을 원할경우 y를 입력해주세요 :")
    if restart_value == "y": pass
    else : print("게임을 종료합니다."), exit()