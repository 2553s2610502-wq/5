import streamlit as st

st.set_page_config(
    page_title="급식 대기시간 확인",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ 급식 대기시간 확인 시스템")

st.write("현재 대기 상황을 확인해보세요.")

# 예외 처리
try:
    current_number = st.number_input(
        "현재 급식실에서 처리 중인 번호",
        min_value=1,
        value=20
    )

    my_number = st.number_input(
        "내 대기번호",
        min_value=1,
        value=25
    )

    avg_time = st.number_input(
        "1명당 평균 소요시간(초)",
        min_value=1,
        value=10
    )

    remaining_people = max(my_number - current_number, 0)
    waiting_minutes = round((remaining_people * avg_time) / 60, 1)

    st.subheader("📊 대기 현황")

    if remaining_people == 0:
        st.success("현재 입장 가능한 상태입니다!")
    else:
        st.info(f"내 앞에 {remaining_people}명 남았습니다.")
        st.info(f"예상 대기시간: 약 {waiting_minutes}분")

    st.divider()

    st.subheader("🍱 오늘의 급식 메뉴")

    menu = [
        "쌀밥",
        "된장찌개",
        "치킨강정",
        "계란말이",
        "배추김치",
        "요구르트"
    ]

    for item in menu:
        st.write(f"• {item}")

    st.divider()

    st.caption("QR 코드를 통해 접속하여 실시간으로 대기시간을 확인할 수 있습니다.")

except Exception as e:
    st.error("오류가 발생했습니다.")
    st.error(str(e))
