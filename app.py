import streamlit as st
from datetime import datetime

st.set_page_config(page_title="익명 새치기 신고 시스템")

st.title("🚨 급식 새치기 익명 신고 시스템")
st.write("신고자는 익명으로 처리되며 기록만 저장됩니다.")

# -----------------------------
# 데이터 저장
# -----------------------------
if "reports" not in st.session_state:
    st.session_state.reports = []

if "report_count" not in st.session_state:
    st.session_state.report_count = 0

# -----------------------------
# 입력
# -----------------------------
reporter = st.text_input("신고자 이름 (기록에는 남지 않음)")
target = st.text_input("새치기한 사람 이름")

if st.button("익명 신고하기"):
    if reporter.strip() == "" or target.strip() == "":
        st.warning("모든 항목을 입력하세요.")
    else:
        st.session_state.report_count += 1

        st.session_state.reports.append({
            "id": st.session_state.report_count,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target": target
        })

        st.success("익명으로 신고가 접수되었습니다!")

# -----------------------------
# 신고 기록
# -----------------------------
st.subheader("📜 신고 기록")

if len(st.session_state.reports) == 0:
    st.info("아직 신고 기록이 없습니다.")
else:
    for r in reversed(st.session_state.reports):
        st.write(f"[익명 신고 {r['id']}] {r['target']} | {r['time']}")
