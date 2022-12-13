import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울 통근, 통학하는 교통수단")

st.write(
   "https://data.seoul.go.kr/dataList/10283/S/2/datasetView.do"
)

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df = pd.read_csv('../cmmute/data.csv', encoding='cp949')
st.write(df)