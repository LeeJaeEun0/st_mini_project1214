import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('전국 지역보건의료기관 현황')

# 파일 가져오기

df = pd.read_csv('./medical_institution/medical_instituntion.csv', encoding='CP949')
df.set_index = df['보건기관명']

# 데이터를 어디에서 가져왔는지
if st.button('data copyright link'):
    st.write('https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=3072692')


# 데이터를 보여줌
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

# 일단 그래프 그려보기
st.title('지역보건의료기관 시에 따른 분류')
fig = plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='시도')
st.pyplot(fig)


# 데이터를 분석하기
st.subheader('시에 따른 분류')
option = st.selectbox(
    'Select Line', 
    (df['시도']))

station_data = df.loc[(df['시도'] == option)]
station_data = station_data[station_data.columns.difference(['시군구', '보건기관명'])]
s_index = station_data.index.tolist()
st.area_chart(station_data.loc[s_index[0]], use_container_width=True
)