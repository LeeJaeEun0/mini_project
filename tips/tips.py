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

fig = plt.figure(figsize=(8, 4))
sns.histplot(data=tips, x='size')
st.pyplot(fig)

