import streamlit as st

# [교정] 무조건 코드 최상단에 배치해야 에러가 나지 않습니다.
st.set_page_config(
    page_title="오늘의 급식 & 알레르기 알리미",
    page_icon="🍱",
    layout="centered"
)

import random
import datetime

# 2. 샘플 데이터
MENUS_DATABASE = {
    "점심": [
        {"name": "돈가스", "allergies": ["대두", "밀", "돼지고기"]},
        {"name": "흑미밥", "allergies": []},
        {"name": "팽이버섯된장국", "allergies": ["대두"]},
        {"name": "양상추샐러드", "allergies": ["키위"]},
        {"name": "배추김치", "allergies": ["새우"]}
    ],
    "저녁": [
        {"name": "짜장면", "allergies": ["밀", "대두", "돼지고기"]},
        {"name": "단무지", "allergies": []},
        {"name": "탕수육", "allergies": ["밀", "돼지고기", "계란"]},
        {"name": "요구르트", "allergies": ["우유"]},
        {"name": "포기김치", "allergies": ["새우"]}
    ]
}

NUTRITION_TIPS = [
    "균형 잡힌 식사는 면역력을 높이는 가장 좋은 방법입니다! 💪",
    "천천히 20번 이상 씹어 먹으면 소화와 두뇌 활동에 도움이 됩니다. 🧠",
    "식사 후 바로 눕기보다는 10분 정도 가볍게 산책을 해보세요. 🚶‍♂️",
    "물은 식사 직전보다는 식간에 자주 마시는 것이 좋습니다. 💧"
]

ALLERGY_LIST = ["계란", "우유", "메밀", "땅콩", "대두", "밀", "고등어", "게", "새우", "돼지고기", "복숭아", "토마토", "아황산류", "호두", "닭고기", "쇠고기", "오징어", "조개류", "잣", "키위"]

# 3. 앱 타이틀 및 소개
st.title("🍱 오늘의 급식 & 알레르기 알리미")
st.caption("오늘의 메뉴를 확인하고, 내 알레르기 유발 성분이 있는지 안전하게 체크하세요!")
st.write("---")

# 4. 사이드바 - 사용자 입력 제어
st.sidebar.header("🔍 식단 조회 설정")

selected_date = st.sidebar.date_input("날짜를 선택하세요", datetime.date.today())
meal_type = st.sidebar.radio("식사 종류", ["점심", "저녁"])

st.sidebar.write("---")
st.sidebar.header("⚠️ 나의 알레르기 정보")
st.sidebar.write("조심해야 할 성분을 체크해 주세요.")

user_allergies = st.sidebar.multiselect(
    "알레르기 유발 물질 선택:",
    options=ALLERGY_LIST,
    default=[]
)

# 5. 메인 화면 - 급식 메뉴 및 알레르기 검증 로직
st.subheader(f"📅 {selected_date.strftime('%Y년 %m월 %d일')} - {meal_type} 메뉴")

try:
    current_menu = MENUS_DATABASE.get(meal_type, [])
    
    if not current_menu:
        st.info("선택하신 날짜의 식단 데이터가 없습니다.")
    else:
        detected_allergies = set()
        st.markdown("### 🍴 식단표")
        
        for item in current_menu:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**• {item['name']}**")
                
            with col2:
                overlap = set(item['allergies']).intersection(set(user_allergies))
                if overlap:
                    st.error(f"⚠️ 주의 ({', '.join(overlap)})")
                    for allergy in overlap:
                        detected_allergies.add(allergy)
                else:
                    if item['allergies']:
                        # [교정] 불안정한 HTML span 태그 대신 Streamlit 공식 컬러 마크다운 사용
                        st.write(f":gray[알레르기: {', '.join(item['allergies'])}]")
                    else:
                        st.caption("성분 없음")
                        
        st.write("---")
        
        if detected_allergies:
            st.warning(f"🚨 **경고:** 오늘 식단에 주의해야 할 알레르기 성분(**{', '.join(detected_allergies)}**)이 포함되어 있습니다! 식사 시 주의하세요.")
        elif user_allergies:
            st.success("✅ **안심:** 오늘 식단에는 선택하신 알레르기 유발 성분이 없습니다.")

except Exception as e:
    st.error(f"앱 실행 중 오류가 발생했습니다. 개발자에게 문의하세요. (오류 내용: {e})")

# 6. 추가 유용한 기능: 오늘의 영양 한 줄 팁
st.write("")
st.info(f"💡 **오늘의 영양 Tip:** {random.choice(NUTRITION_TIPS)}")
