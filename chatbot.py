# Noneo_chatbot
import random

# 질문과 정답의 데이터셋 (논어 예시)
questions_answers = {
    "공자의 이웃에 대한 생각은?": "네 자신이 받고 싶은 대로 대접하라.",
    "공자의 지혜의 출발점은?": "바로 존재이다.",
    "공자의 도덕적 가치는?": "仁을 구현하는 것이다."
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

