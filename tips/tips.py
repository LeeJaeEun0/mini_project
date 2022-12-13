import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("tips")

tips = sns.load_dataset('tips')
st.write(tips)

sns.barplot(x='day', y='size', data=tips)
plt.show()
sns.barplot(x='size', y='time', data=tips)
plt.show()