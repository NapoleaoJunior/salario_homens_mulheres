import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("dataset_salarios.xlsx")

# Visualizar as primeiras linhas
print(df.head())

# Verificar os valores únicos na coluna de sexo
print(df['Sexo'].unique())