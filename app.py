import streamlit as st

st.set_page_config(
    page_title="급식 예약 시스템",
    page_icon="🍽️",
    layout="centered"
)

# =========================
# 🎨 배경 & 스타일 CSS ([교정] 에러 원인이 되던 내부 주석 전부 제거)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)),
    url('https://images.unsplash.com/photo-1498837167922-ddd27525d352');
    background-size: cover;
}

h1 {
    text-align: center;
    color: #2E7D32;
    font-size: 40px;
}

.stMarkdown p {
    text-align: center;
    font-size: 18px;
}

div[data-baseweb="select"], input {
    border-radius: 10px !important;
}

.stButton>button {
    background-color: #43A047;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 12px;
    border: none;
    width: 100%;
}

.stButton>button:hover {
    background-color: #2E7D32;
    transform: scale(1.02);
    transition: 0.2s;
}

.card {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    margin: 8px 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# 📌 앱 제목
# =========================
st.title("🍽️ 급식 예약 시스템")
st.write("오늘 급식을 먹을 학생은 정보를 입력하고 예약하세요!")

# =========================
# 📦 세션 초기화
# =========================
if "reservations" not in st.session_state:
    st.session_state.reservations = []

# =========================
# 📝 입력 폼
# =========================
with st.form("reservation_form"):
    grade = st.selectbox("학년", [1, 2, 3, 4, 5, 6])
    classroom = st.number_input("반", min_value=1, max_value=20, step=1)
    number = st.number_input("번호", min_value=1, max_value=50, step=1)

    submit = st.form_submit_button("🍱 급식 예약하기")

# =========================
# ✅ 예약 처리
# =========================
if submit:
    student_id = f"{grade}-{classroom}-{number}"

    existing_ids = [item["id"] for item in st.session_state.reservations]

    if student_id in existing_ids:
        st.error("❌ 이미 예약한 학생입니다!")
    else:
        st.session_state.reservations.append({
            "id": student_id,
            "grade": grade,
            "classroom": classroom,
            "number": number
        })
        st.success("✅ 예약 완료! 맛있는 급식 드세요 🍱")

# =========================
# 📊 예약 현황
# =========================
st.divider()
st.subheader("📋 예약 현황")

if st.session_state.reservations:
    for student in st.session_state.reservations:
        st.markdown(f"""
        <div class="card">
            🍽️ {student['grade']}학년 {student['classroom']}반 {student['number']}번
        </div>
        """, unsafe_allow_html=True)

    st.info(f"총 예약 인원: {len(st.session_state.reservations)}명")
else:
    st.info("아직 예약한 학생이 없습니다.")
