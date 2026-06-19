import pandas as pd
import datetime
import time
import streamlit as st  # [교정] 누락되었던 라이브러리 추가

# 페이지 설정
st.set_page_config(
    page_title="급식줄 효율적 구축 시스템",
    page_icon="🍔",
    layout="centered"
)

# 세션 상태 초기화
if 'reports' not in st.session_state:
    st.session_state.reports = pd.DataFrame(columns=['시간', '인원수', '혼잡도'])

# 앱 타이틀
st.title("🍔 스마트 급식줄 알림이")
st.markdown("실시간 혼잡도를 확인하고 대기 시간을 예측하여 효율적으로 식사하세요!")
st.markdown("---")

# --- 1. 실시간 상태 대시보드 ---
st.subheader("📊 현재 식당 혼잡도")

now = datetime.datetime.now()
current_time_str = now.strftime("%H:%M:%S")

if not st.session_state.reports.empty:
    latest_report = st.session_state.reports.iloc[-1]
    current_wait_people = int(latest_report['인원수'])
else:
    current_wait_people = 15 

avg_time_per_person_sec = 12
estimated_wait_time = round((current_wait_people * avg_time_per_person_sec) / 60)

if current_wait_people < 15:
    status = "🟢 원활"
    status_color = "green"
    msg = "지금 바로 가시면 기다리지 않고 식사할 수 있습니다!"
elif current_wait_people <= 35:
    status = "🟡 보통"
    status_color = "orange"
    msg = "약간의 대기가 있습니다. 이동 시간을 고려해 출발하세요."
else:
    status = "🔴 혼잡"
    status_color = "red"
    msg = "줄이 매우 깁니다! 잠시 후 방문하시는 것을 추천합니다."

col1, col2 = st.columns(2)
with col1:
    st.metric(label="현재 예상 대기 인원", value=f"{current_wait_people} 명")
with col2:
    st.metric(label="예상 대기 시간", value=f"약 {estimated_wait_time} 분")

st.markdown(f"""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid {status_color};">
    <h4 style="margin: 0; color: {status_color};">{status} 상태</h4>
    <p style="margin: 5px 0 0 0; color: #31333F;">{msg}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- 2. 실시간 혼잡도 제보 ---
st.subheader("✍️ 지금 급식줄은 어떤가요? (실시간 제보)")

with st.form(key="report_form", clear_on_submit=True):
    reported_people = st.slider("눈대중으로 보이는 대기 인원수를 선택해주세요.", min_value=0, max_value=80, value=15)
    # [교정] 중복 대입(=) 오타 수정
    submit_button = st.form_submit_button(label="제보하기")

    if submit_button:
        try:
            if reported_people < 15:
                rep_status = "원활"
            elif reported_people <= 35:
                rep_status = "보통"
            else:
                rep_status = "혼잡"
            
            new_data = pd.DataFrame([{
                '시간': now.strftime("%H:%M"),
                '인원수': reported_people,
                '혼잡도': rep_status
            }])
            
            st.session_state.reports = pd.concat([st.session_state.reports, new_data], ignore_index=True)
            st.success("제보가 성공적으로 반영되었습니다!")
            time.sleep(0.5)
            st.rerun()
            
        except Exception as e:
            # [교정] 존재하지 않는 content 인자 제거
            st.error(f"데이터 처리 중 오류가 발생했습니다: {e}")

# --- 3. 오늘 기록된 데이터 추이 ---
st.markdown("---")
st.subheader("📈 오늘 시간대별 대기 인원 추이")

if not st.session_state.reports.empty:
    chart_data = st.session_state.reports.set_index('시간')
    st.line_chart(chart_data['인원수'])
    
    with st.expander("전체 제보 이력 보기"):
        st.dataframe(st.session_state.reports.tail(10), use_container_width=True)
else:
    st.info("아직 기록된 데이터가 없습니다. 위의 폼에서 첫 제보를 남겨보세요!")
