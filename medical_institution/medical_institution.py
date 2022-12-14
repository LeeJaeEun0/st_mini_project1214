import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('전국 지역보건의료기관 현황')

# 파일 가져오기

df = pd.read_csv('./medical_institution/medical_instituntion.csv', encoding='CP949')
df.set_index = df['우편번호']

# 데이터를 어디에서 가져왔는지
if st.button('data copyright link'):
    st.write('https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=3072692')


# 데이터를 보여줌
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)