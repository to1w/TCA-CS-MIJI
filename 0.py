import random

def guess_number():

    number = random.randint(1, 100)
    attempts = 0  

    print("1부터 100 사이의 숫자를 맞춰부수유!")

    while True:

        guess = input("숫자를 입력하세요: ")

        if not guess.isdigit():
            print("숫자만 입력해주세요.")
            continue

        guess = int(guess)
        attempts += 1

        if guess > number:
            print("더 작은 숫자입니다.")
     
        elif guess < number:
            print("더 큰 숫자입니다.")
       
        else:
            print(f"축하합니다! {attempts}번 만에 맞추셨습니다.")
            break

guess_number()
