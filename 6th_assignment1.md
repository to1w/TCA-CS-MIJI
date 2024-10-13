# 📌 Assignment 4-2

## 1. 제목

ChatGPT를 활용한 자료구조 선택과 최적화

## 2. 이름

심미지(Miji)

## 3. 제출일

24.10.13 (일)

## 4. 과제 목표

> 스스로 생각하는 과제의 목표를 작성해 주세요.

자료구조를 잘 활용하여 학생들 성적과 성적을 관리하는 프로그램 만들기.

## 5. ChatGPT 활용

### 👉 질문 내용

> ChatGPT에게 했던 질문을 기록합니다. (예. 여러 과목을 담당하는 선생님을 효율적으로 관리하기 위한 자료구조는 무엇이 좋을까요?)

학생과 성적을 효율적으로 관리하기 위한 자료구조는 뭐야?

### 👉 ChatGPT 답변 요약

> ChatGPT가 제공한 답변을 간단히 요약합니다. (예. 딕셔너리가 적합하며, 각 과목을 키로 하고 선생님들의 목록을 값으로 사용하는 방법이 좋다고 조언을 받았습니다.)

학생과 성적 관리는 리스트, 딕셔너리, 트리, 우선순위 큐) 같은 자료구조를 사용하면 효율적이라는 답변을 받았다.

## 6. 자료구조 선택 이유

> ChatGPT의 조언을 기반으로 선택한 자료구조와 그 이유를 서술합니다.

딕셔너리를 선택하였다. 그 이유는 딕션어리로 프로그림을 만들어야 빠른 조회가 가능하기 때문이다.

## 7. 코드 작성 과정

> 코드를 작성하는 과정을 적습니다.

students = {}

def add_student(name, score):
    students[name] = score
    print(f"학생 {name}의 성적 {score}점이 추가되었습니다.")

def get_student_score(name):
    if name in students:
        return f"{name}의 성적은 {students[name]}점입니다."
    else:
        return f"{name} 학생을 찾을 수 없습니다."

def delete_student(name):
    if name in students:
        del students[name]
        print(f"학생 {name}이(가) 삭제되었습니다.")
    else:
        print(f"{name} 학생을 찾을 수 없습니다.")

def print_all_students():
    if students:
        print("전체 학생 목록:")
        for name, score in students.items():
            print(f"학생: {name}, 성적: {score}")
    else:
        print("등록된 학생이 없습니다.")

add_student("Miji", 90)
add_student("Alice", 85)
print(get_student_score("Miji"))
delete_student("Alice")
print_all_students()


## 8. 코드 실행 결과

> 프로그램 실행 결과를 캡쳐 이미지로 첨부합니다.

![image](https://github.com/user-attachments/assets/266174c2-2209-4783-a566-7108a669a7d4)



## 9. 문제 해결 과정 및 배운점

> ChatGPT와의 상호작용을 통해 얻은 인사이트와 프로그램을 개선하는 과정에서 배운 내용을 정리합니다.

ChatGPT를 활용해 어떤 상황에서 어떤 자료구조를 사용해야 효율적인지를 알았다.
