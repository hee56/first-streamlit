import streamlit as st
import random
import pandas as pd

st.title("여러 가지 입력창")

st.button("리셋 버튼", type="primary")

if st.button("랜덤 숫자 생성"):
    st.write(random.random())
else:
    st.write("Goodbye")


text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)

st.link_button("Go to gallery", "https://streamlit.io/gallery")

agree = st.checkbox("동의합니다.")

if agree:
    st.write("동의하셨습니다. 다음 문항으로 넘어가주세요.")
else:
    st.write("동의 버튼을 먼저 클릭해주세요.")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"])

st.write("You selected:", options)

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

number = st.number_input("숫자를 입력하세요.", step = 1)
st.write("The current number is ", number)

title = st.text_area("Movie title", "눈물의 여왕")
st.write(title, "을 보셨군요! 저도요!")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    #data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding='euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    #data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding='euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)