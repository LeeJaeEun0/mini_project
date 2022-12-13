import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("tips 문화")

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
tips = sns.load_dataset('tips')
st.write(tips)