### 창업아이템 
 * ai기술을 활용하여 경전을 스스로 학습할 수 있는 멀티모달 챗봇

### 고객가치에 대해 생각할 점
 * 내가 제공하는 서비스를 통해 고객은 어떤 가치를 얻을 수 있는가?
   → 왜 그 가치가 사람들에게 필요할 것이라고 생각했는가?   
   → 현재 사람들은 어떤 마음을 가지고 있는가?

## 고객 분석 시 고려할 점
 * 목표고객은?
 * 목표고객의 특성은?

### 데이터가 뛰어노는 AI 놀이터, 캐글

##캐글 관련 내용 링크 

#캐글 관련 내용 링크[이동하기]

|클래스 이름| 내용 | 저장소 링크|
| --- | --- | --- |
|파이썬 시작하기-클래스|파이썬 왕초보를 위한 파이썬 기본 수업|---|

### 핑크를 걸고 싶다.

2022년 데이터 분석 내용 정리 [이동](https://github.com/yoonheeja/test_2406/edit/main/README.md)

### 수평선 넣기
---

### 이미지 삽입
![강아지](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHQQdAY4HvcdOtRxApXStj7oRvUNKlATHpWA&s)

### 이미지 삽입 - 크리도 조정
<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHQQdAY4HvcdOtRxApXStj7oRvUNKlATHpWA&s" width = "300" height = "300">

## 링크 걸기, 내 레포에 pdf 연결
[논문](./blob/main/2015.pdf)

###잘 안된다.







# Noneo_chatbot
import random

# 질문과 정답의 데이터셋 (논어 예시)
questions_answers = {
    "공자가 이웃에 대한 생각은?": "네 자신을 원하는 대로 대접하라.",
    "공자가 지혜의 출발점은?": "바로 존재.",
    "공자의 도덕적 가치는?": "상대에게 대접하는 것이다."
}

# RAG 지표에 따른 메시지
rag_messages = {
    "진행 중인": "잘 하고 있어요! 계속해서 공부해 주세요.",
    "위험한": "잘못된 대답이 있습니다. 다시 공부해 보세요.",
    "영향이 적음": "좋은 진행이에요! 더 많은 질문에 대한 답변을 해 보세요."
}

def ask_question():
    # 랜덤하게 질문 선택
    question = random.choice(list(questions_answers.keys()))
    answer = input(question + "\n")  # 질문 출력 및 답변 입력
    expected_answer = questions_answers[question]
    if answer.strip() == expected_answer:
        return "진행 중인"
    else:
        return "위험한"

def main():
    print("논어 학습 챗봇에 오신 것을 환영합니다!\n")
    print("챗봇이 논어 관련 질문을 하고, 답변을 입력해주세요.\n")
    
    while True:
        rag_status = ask_question()
        print(rag_messages[rag_status])  # RAG 지표에 따른 메시지 출력
        input("다음 질문을 받으려면 엔터를 눌러주세요.\n")

if __name__ == "__main__":
    main()

