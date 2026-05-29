import random
import streamlit as st

st.set_page_config(page_title="마법의 소라고동", page_icon="🐚")

answers = [
    "네",
    "안돼",
    "아마도",
    "다시 물어보세요",
    "좋은 결과가 있을 거예요",
    "오늘은 쉬는 게 좋아요",
    "도전해보세요",
]

st.title("🐚 마법의 소라고동")
st.write("질문을 입력하고 버튼을 눌러보세요!")

question = st.text_input("질문")

if st.button("대답 듣기"):
    if question.strip() == "":
        st.warning("질문을 입력해주세요!")
    else:
        st.success(random.choice(answers))
