import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="마법의 소라고동",
    page_icon="🐚"
)

st.title("🐚 마법의 소라고동")
st.write("질문을 입력하면 소라고동이 답해줍니다.")

# API 키 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

except Exception as e:
    st.error(f"API 설정 오류: {e}")
    st.stop()

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 채팅 표시
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
prompt = st.chat_input("질문을 입력하세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # 소라고동 전용 프롬프트
        system_prompt = """
        너는 '마법의 소라고동'이다.
        사용자의 질문에 짧고 신비롭게 대답한다.
        답변은 한두 문장 이내로 한다.
        """

        response = model.generate_content(
            f"{system_prompt}\n\n사용자 질문: {prompt}"
        )

        answer = response.text.strip()

    except Exception as e:
        answer = f"오류가 발생했습니다: {e}"

    # 응답 표시
    with st.chat_message("assistant"):
        st.markdown(answer)

    # 기록 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
