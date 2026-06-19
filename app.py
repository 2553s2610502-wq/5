import streamlit as st
from datetime import datetime

st.set_page_config(page_title="급식 QR 대기 시스템", layout="centered")

# -----------------------------
# 초기 데이터 저장 (세션)
# -----------------------------
if "queue" not in st.session_state:
    st.session_state.queue = []

if "reports" not in st.session_state:
    st.session_state.reports = []

# -----------------------------
# 제목
# -----------------------------
st.title("🍱 급식 줄서기 QR 시스템")
st.caption("대기 현황 확인 + 새치기 신고 기능")

# -----------------------------
# 대기 등록
# -----------------------------
st.subheader("📌 줄 서기 등록")

name = st.text_input("이름 입력")

if st.button("줄 서기 등록"):
    if name.strip() == "":
        st.warning("이름을 입력하세요.")
    else:
        if name in st.session_state.queue:
            st.warning("이미 줄에 등록되어 있습니다.")
        else:
            st.session_state.queue.append(name)
            st.success(f"{name}님이 줄에 등록되었습니다!")

# -----------------------------
# 대기 현황
# -----------------------------
st.subheader("📊 현재 대기 현황")

if len(st.session_state.queue) == 0:
    st.info("현재 대기 인원이 없습니다.")
else:
    st.write(f"현재 대기 인원: **{len(st.session_state.queue)}명**")

    for i, person in enumerate(st.session_state.queue, start=1):
        st.write(f"{i}. {person}")

# -----------------------------
# 내 순번 확인
# -----------------------------
st.subheader("🔎 내 순번 확인")

check_name = st.text_input("내 이름 입력 (순번 확인용)", key="check")

if st.button("순번 확인"):
    if check_name in st.session_state.queue:
        idx = st.session_state.queue.index(check_name) + 1
        st.success(f"{check_name}님의 순번은 {idx}번입니다.")
    else:
        st.warning("줄에 등록되어 있지 않습니다.")

# -----------------------------
# 새치기 신고 기능
# -----------------------------
st.subheader("🚨 새치기 신고")

reporter = st.text_input("신고자 이름")
target = st.text_input("신고 대상 이름")

if st.button("신고하기"):
    if reporter.strip() == "" or target.strip() == "":
        st.warning("신고자와 대상 이름을 모두 입력하세요.")
    else:
        report = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "reporter": reporter,
            "target": target
        }
        st.session_state.reports.append(report)
        st.success("신고가 접수되었습니다.")

# -----------------------------
# 신고 기록 출력
# -----------------------------
st.subheader("📜 신고 기록")

if len(st.session_state.reports) == 0:
    st.info("신고 기록이 없습니다.")
else:
    for r in reversed(st.session_state.reports):
        st.write(f"[{r['time']}] {r['reporter']} → {r['target']} 신고")
