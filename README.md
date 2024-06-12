# Noneo_chatbot
class LunyuChatbot:
    def __init__(self):
        self.lunyu = {
            "공자가 말하였다": ["학문이 깊은 사람은 의심스러운 것을 좋아하고, 얕은 사람은 이해하지 못하는 것을 좋아한다.", "지식이 없는 사람은 자신을 모른다.", "지식이 없는 사람은 자신을 모른다."],
            "자로가 말하였다": ["사람은 학문을 통해 자신을 알 수 있다.", "사람은 학문을 통해 자신을 알 수 있다."]
        }

    def get_response(self, user_input):
        for key in self.lunyu.keys():
            if key in user_input:
                return random.choice(self.lunyu[key])
        return "죄송합니다, 그에 대한 답변을 찾을 수 없습니다."

chatbot = LunyuChatbot()
while True:
    user_input = input("질문을 입력하세요: ")
    print(chatbot.get_response(user_input))
