import pandas as pd
import datetime
import streamlit as st

st.set_page_config(
    page_title="급식줄 효율적 구축 시스템",
    page_icon="🍔",
    layout="centered"
)

# =====================
# 세션 초기화
# =====================
if "reports" not in st.session_state:
    st.session_state.reports = pd.DataFrame(
        columns=["시간", "인원수", "혼잡도"]
    )

# =====================
# 타이틀
# =====================
st.title("🍔 스마트 급식줄 알림이")
st.markdown("실시간 혼잡도 + 대기시간 예측 시스템")
st.markdown("---")

# =====================
# 현재 상태
# =====================
st.subheader("📊 현재 식당 혼잡도")

now = datetime.datetime.now()

if not st.session_state.reports.empty:
    latest_report = st.session_state.reports.iloc[-1]
    current_wait_people = int(latest_report["인원수"])
else:
    current_wait_people = 15

avg_time_per_person_sec = 12
estimated_wait_time = round((current_wait_people * avg_time_per_person_sec) / 60)

if current_wait_people < 15:
    status, status_color, msg = "🟢 원활", "green", "지금 바로 가도 됩니다!"
elif current_wait_people <= 35:
    status, status_color, msg = "🟡 보통", "orange", "약간 대기가 있습니다."
else:
    status, status_color, msg = "🔴 혼잡", "red", "줄이 매우 깁니다!"

col1, col2 = st.columns(2)

with col1:
    st.metric("현재 예상 대기 인원", f"{current_wait_people} 명")

with col2:
    st.metric("예상 대기 시간", f"{estimated_wait_time} 분")

st.markdown(f"""
<div style="background-color:#f0f2f6;padding:15px;border-radius:10px;
border-left:5px solid {status_color};">
<h4 style="color:{status_color};margin:0;">{status}</h4>
<p style="margin:5px 0 0 0;">{msg}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================
# 제보 시스템
# =====================
st.subheader("✍️ 급식줄 제보")

with st.form("report_form", clear_on_submit=True):
    reported_people = st.slider(
        "대기 인원수",
        0, 80, 15
    )

    submit_button = st.form_submit_button("제보하기")

    if submit_button:

        # ✔ 시간은 “클릭 시점” 기준
        submit_time = datetime.datetime.now()

        if reported_people < 15:
            rep_status = "원활"
        elif reported_people <= 35:
            rep_status = "보통"
        else:
            rep_status = "혼잡"

        new_row = pd.DataFrame([{
            "시간": submit_time,   # ✔ datetime 그대로 저장 (핵심 개선)
            "인원수": int(reported_people),
            "혼잡도": rep_status
        }])

        st.session_state.reports = pd.concat(
            [st.session_state.reports, new_row],
            ignore_index=True
        )

        st.success("제보 완료!")

# =====================
# 그래프
# =====================
st.markdown("---")
st.subheader("📈 대기 인원 추이")

if not st.session_state.reports.empty:

    chart_data = st.session_state.reports.copy()

    # ✔ datetime 기준 정렬 (핵심 개선)
    chart_data = chart_data.sort_values(by="시간")

    chart_data = chart_data.set_index("시간")

    st.line_chart(chart_data["인원수"])

    with st.expander("전체 기록"):
        st.dataframe(st.session_state.reports.tail(10))

else:
    st.info("아직 데이터가 없습니다.")
