import streamlit as st
from datetime import datetime

st.set_page_config(page_title="새치기 신고 시스템")

st.title("🚨 급식 새치기 신고 시스템")
st.write("새치기를 신고하면 기록이 저장됩니다.")

# -----------------------------
# 신고 저장 공간
# -----------------------------
if "reports" not in st.session_state:
    st.session_state.reports = []

# -----------------------------
# 신고 입력
# -----------------------------
reporter = st.text_input("신고자 이름")
target = st.text_input("새치기한 사람 이름")

if st.button("신고하기"):
    if reporter.strip() == "" or target.strip() == "":
        st.warning("모든 항목을 입력하세요.")
    else:
        st.session_state.reports.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "reporter": reporter,
            "target": target
        })
        st.success("신고가 접수되었습니다!")

# -----------------------------
# 신고 기록 출력
# -----------------------------
st.subheader("📜 신고 기록")

if len(st.session_state.reports) == 0:
    st.info("아직 신고 기록이 없습니다.")
else:
    for r in reversed(st.session_state.reports):
        st.write(f"[{r['time']}] {r['reporter']} → {r['target']}")
