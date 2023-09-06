import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('./Bases_de_dados/credit_data.csv')

base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92

base_credit['age'].fillna(base_credit['age'].mean(), inplace=True)


x_credits = base_credit.iloc[:, ]