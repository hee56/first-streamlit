import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("데이터 시각화")
'''
csv_file = st.file_uploader(label = "펭귄 데이터를 업로드해주세요. 단, csv 파일만 가능합니다.")
if csv_file is not None:
    csv_file_df = pd.read_csv(csv_file, encoding='euc-kr')
    st.write(csv_file_df.head(5))

chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.write(chart_data)
st.write(csv_file_df['종'].value_counts())
st.bar_chart(csv_file_df['종'].value_counts())
st.bar_chart(csv_file_df['서식지'].value_counts())


fig, ax = plt.subplots()
sns.histplot(csv_file_df.bill_length_mm, binrange=[30,60], binwidth = 2.5)

st.pyplot(fig)
'''

csv_file = st.file_uploader(label = "데이터를 업로드해주세요. 단, csv 파일만 가능합니다.")
if csv_file is not None:
    csv_file_df = pd.read_csv(csv_file, encoding='euc-kr')
    st.write(csv_file_df.head(5))

column = st.radio(label = "열 이름을 선택해주세요.", options=csv_file_df.columns)
st.subheader(column, "의 분포를 그려보겠습니다.!")
st.bar_chart(csv_file_df[column].value_counts())

fig, ax = plt.subplots()
sns.histplot(csv_file_df.bill_length_mm, binrange=[30,60], binwidth = 2.5)

st.pyplot(fig)