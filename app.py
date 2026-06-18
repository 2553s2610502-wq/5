import streamlit as st

st.set_page_config(
    page_title="급식 대기시간 안내",
    page_icon="🍱",
    layout="centered"
)

st.title("🍱 급식 대기시간 안내")

st.write("현재 배식 상황을 확인해보세요!")

try:
    current_number = st.number_input(
        "현재 배식 중인 번호",
        min_value=1,
        value=50,
        step=1
    )

    my_number = st.number_input(
        "내 번호",
        min_value=1,
        value=60,
        step=1
    )

    if my_number < current_number:
        st.success("✅ 이미 차례가 지났거나 현재 배식 중입니다!")

        progress = 100

    else:
        remaining = my_number - current_number

        wait_seconds = remaining * 15
        wait_minutes = wait_seconds // 60
        wait_remain_seconds = wait_seconds % 60

        st.subheader("📢 대기 현황")

        st.metric(
            label="남은 인원",
            value=f"{remaining}명"
        )

        st.metric(
            label="예상 대기시간",
            value=f"{wait_minutes}분 {wait_remain_seconds}초"
        )

        progress = (current_number / my_number) * 100
        progress = min(progress, 100)

    st.subheader("📊 진행 상황")
    st.progress(int(progress))
    st.write(f"진행률: {progress:.1f}%")

except Exception:
    st.error("입력값을 확인해주세요.")

st.divider()

st.subheader("🍽️ 오늘의 급식")

menu = [
    "쌀밥",
    "된장찌개",
    "돈까스",
    "배추김치",
    "샐러드",
    "요구르트"
]

for food in menu:
    st.write(f"• {food}")

st.divider()

st.caption("학교 급식 대기시간 예측 서비스")
