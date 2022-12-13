import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("tips")

tips = sns.load_dataset('tips')
# st.write(tips)

sns.histplot(data=tips, x='size')