
import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="숫자 맞추기 게임",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 숫자 맞추기 게임")

# 세션 상태 초기화
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "game_clear" not in st.session_state:
    st.session_state.game_clear = False

# 설명
st.write("1부터 100 사이 숫자를 맞춰보세요!")

# 입력
guess = st.number_input(
    "숫자 입력",
    min_value=1,
    max_value=100,
    step=1
)

# 확인 버튼
if st.button("확인"):

    if not st.session_state.game_clear:

        st.session_state.attempts += 1

        if guess < st.session_state.target_number:
            st.warning("📉 더 큰 숫자입니다!")

        elif guess > st.session_state.target_number:
            st.warning("📈 더 작은 숫자입니다!")

        else:
            st.session_state.game_clear = True
            st.success(
                f"🎉 정답입니다! "
                f"{st.session_state.attempts}번 만에 성공!"
            )

# 현재 시도 횟수
st.info(f"시도 횟수: {st.session_state.attempts}")

# 재시작 버튼
if st.button("다시 시작"):

    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_clear = False

    st.rerun()
