##################################################################
#  streamlit/01_streamlit_chat_exam.py
#  챗봇 대화 관련 위젯 
# 1. chat_input() : 사용자 입력을 받는 위젯
# 2. chat_message() : 메세지를 container(내용 창)에 입력하는 위젯.

# chat_input(): str
# - 사용자 입력을 받는 위젯이다.
# - 사용자가 입력한 내용은 엔터를 치면 반환되고, 입력폼에 작성된 글은 지워진다.
# - 코드가 어디에 위치하든지 상관없이 맨 아래에 위치한다.
# - 주요파라미터
#    - placeholder:str - 입력폼에 표시할 힌트
#    - key:str|int - 위젯의 고유 식별자
#    - max_chars: int - 최대 입력 글자수. None(default): 제한 없음
#    - on_submit: Callable - 엔터를 눌렀을 때(submit) 호출할 함수
# - https://docs.streamlit.io/develop/api-reference/chat/st.chat_input

# chat_message(name, *, avatar=None): Container
# - 메세지를 container(내용 창)에 입력하는 위젯.
# - 반환된 container에 write() 하거나 with 문을 이용해 write() 한다.
# - parameter
#    - name:str =  입력하는 메세지 작성자. ("assistant", "ai", "human", "user" or str)
#        - "assistant", "ai": 챗봇이 작성한 메세지, "human", "user": 사용자가 작성한 메세지
#    - avatar: str|st.image|None 
#        - 문자열, emoji, 이미지 등을 사용하여 아바타 이미지를 표현한다.
#        - 메세지 작성자를 표현하는 아바타 이미지.
#        - avatar=None 이면 name에 따라 결정된다. 
#              - name이 user, human, assistant, ai 일 경우 정해진 아이콘이 사용된다.
#              - name이 다른 문자열일 경우 첫번째 글자를 아바타로 사용한다.
#        - avatar 를 지정하면 지정한 avatar를 사용한다.
#              - 단 이름이 user, human, assistant, ai 일 경우 default avatar 가 나오고 그 뒤에 지정한 avatar가 나온다.
# - https://docs.streamlit.io/develop/api-reference/chat/st.chat_message

# st.session_state: 사용자의 상태를 저장하는 객체
#   - 페이지가 reload(rerun) 되더라도 유지 되야하는 값들을 저장하는 저장소 역할.
#       - 변수에 저장된 값은 rerun시 사라지게 된다. 그런데 rerun 후에도 그 값이 유지 되어야 하는 경우가 있다. 이런 값들을 저장하는 저장소.
#       - dictionary 형식으로 key=value 형태로 값을 저장한다.
#   - key 가 있는지 여부 확인
#       - in 연산자를 이용해 확인한다. `if "key" in st.session_state:` 형식으로 확인.
#   - 값 조회
#       - st.session_state.key 또는 st.session_state['key'] 를 이용해 조회한다.
#   - 값 저장
#       - st.session_state.key = value 또는 st.session_state['key'] = value 를 이용해 저장한다.
#       - 값을 저장하려는 key가 없으면 KeyError 발생한다. 그래서 미리 key를 생성해 놓고 사용해야 한다.
# 
#   - https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
##################################################################
import streamlit as st
import random

idx = random.randint(0, 9)
chatbot_message_list = ["오늘 날씨가 어떤가요?",
"점심으로 뭘 먹으면 좋을까요?",
"집에서 할 수 있는 간단한 운동은 뭐가 있나요?",
"요즘 인기 있는 드라마 추천해 줄 수 있나요?",
"효과적으로 공부하려면 어떻게 해야 하나요?",
"주말에 어디로 놀러 가면 좋을까요?",
"잠이 안 올 때는 어떻게 하면 좋을까요?",
"효율적으로 정리정돈을 하려면 뭐부터 해야 하나요?",
"건강에 좋은 간식으로는 어떤 게 있나요?",
"스트레스를 푸는 좋은 방법이 있을까요?"]

ai_message = chatbot_message_list[idx] # LLM 서비스에 요청 결과(가상으로 list이용)

st.title("ChatBot 위젯 튜토리얼")


## 사용자 질문(prompt)를 입력받기 - chat_input()
prompt = st.chat_input("User:") 

if prompt:# is not None:
    #  질문(prompt)과 답변(ai_message) 를 chat container(채팅창)에 출력
    # container = st.chat_message("user")  # container를 가져오기. role: "user" -> 입력자를 구분하기 위한 값.
    # container.write(prompt)              # container에 글을 출력.
    with st.chat_message("user"):
        st.write(prompt) # with 문에서 생성한 container에 출력.
    
    # container = st.chat_message("ai")
    # container.write(ai_message)
    with st.chat_message("ai"):
        st.write(ai_message)


















