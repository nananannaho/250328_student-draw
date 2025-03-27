import streamlit as st
import random


st.set_page_config(page_title="학생 뽑기", page_icon="🎲", layout="centered")


st.title("학생 뽑기 게임 🎲")


st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 15px 32px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>label {
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    .stTitle {
        color: #2e8b57;
    }
    .stMarkdown {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


students = st.number_input("학생 수 입력:", min_value=1, step=1, format="%d", key="student_count")


students_list = list(range(1, students + 1))


random.shuffle(students_list)


if 'index' not in st.session_state:
    st.session_state.index = 0  # 처음에는 0번째 인덱스부터 시작
    st.session_state.students_list = students_list  # 학생 리스트 저장


if st.button("학생 뽑기 시작"):
    st.session_state.index = 0  # "학생 뽑기 시작"을 누르면 인덱스를 0으로 초기화
    st.session_state.students_list = students_list  # 학생 리스트를 다시 섞어 초기화


if st.session_state.index < len(st.session_state.students_list):
    current_student = st.session_state.students_list[st.session_state.index]
    st.write(f"**{st.session_state.index + 1}번째 학생**: {current_student}")

    
    if st.button("다음 학생 뽑기 ➡️"):
        st.session_state.index += 1  # 인덱스 증가하여 다음 학생으로 이동
else:
    st.success("모든 학생이 뽑혔습니다! 🎉")
