import pandas as pd
import numpy as np
import sklearn as sl

df= pd.read_csv('house_prediction.csv')
# df.head()
# print(df)

# df.shape
# df.info()
# df.isnull().sum()

# df.columns

# df.dtypes

# df.dropna(inplace=True)
# df.isnull().sum()


# print(df['bedRoom'].unique())

# df_filter = df[(df['bedRoom']==1)]
# df_one_bedroom_house = df_filter.sort_values(by='bedRoom',ascending=False)
# print("a BEDROOM house in Gurugram:\n")
# print(df_one_bedroom_house[['bedRoom','society']].to_string(index=False))


import matplotlib.pyplot as plt
import seaborn as sns

df_sorted = df[df['bedRoom'] == 2]

plt.figure(figsize=(10, 6))


sns.countplot(x='society', data=df_sorted, palette='Blues_d')

plt.title('Number of 2-Bedroom Properties by Society', fontsize=16,color="RED",loc='right')
plt.xlabel('Society', fontsize=30,loc= 'right',color='BLUE')
plt.ylabel('Count of Properties', fontsize=12,loc='top',color='BLUE')
plt.xticks(rotation=90, fontsize=10)  # Rotate x-axis labels if necessary
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

