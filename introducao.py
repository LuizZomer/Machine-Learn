import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('Bases_de_dados/credit_data.csv')

# print(base_credit.head(10))
# print(base_credit.tail(10))
# print(base_credit.describe())
# print(base_credit[base_credit['income'] >= 69995.685578])
# print(base_credit[base_credit['loan'] <= 1.377630])

# print(np.unique(base_credit['default'], return_counts=True))

# print(sns.countplot(x = base_credit['default']))

# plt.hist(x = base_credit['age']);

# plt.hist(x = base_credit['income'])

# plt.hist(x = base_credit['loan'])

# plt.show()

# grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='default')

# grafico.show()

# Apagando os dados inconsistentes
# base_credit3 = base_credit.drop(base_credit[base_credit["age"] < 0].index)

# print(base_credit3.loc[base_credit3['age'] < 0])

# print(base_credit['age'][base_credit['age'] > 0].mean())

base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92

# print(base_credit.loc[base_credit['age'] < 0])
# print(base_credit.head(27))

plt.hist(base_credit['age'])
plt.show()