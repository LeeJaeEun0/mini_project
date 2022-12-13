import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
# st.write(tips)
st.write(
    '''
    # tips 데이터셋을 이용한 데이터 시각화
    ## tips 데이터
    '''
)
st.write(tips)

st.write(
    '''
    ### tips의 total_bill 빈도수
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.histplot(data=tips, x='total_bill')
st.pyplot(fig)

st.write(
    '''
    ### 식사 인원수
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.histplot(data=tips, x='size')
st.pyplot(fig)

st.write(
    '''
    ### 전체적인 그래프
    '''
)
sns.pairplot(data = tips)