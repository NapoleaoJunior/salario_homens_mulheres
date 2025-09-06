import pandas as pd
import numpy as np

# Função de limpeza
def limpar_dados(df):
    df['Sexo'] = df['Sexo'].str.strip().str.lower()
    df['Sexo'] = df['Sexo'].replace({
        'masculino': 'Masculino',
        'feminino': 'Feminino'
    })
    df = df[df['Sexo'].isin(['Masculino', 'Feminino'])]
    df = df[pd.to_numeric(df['Salario'], errors='coerce').notnull()]
    df['Salario'] = df['Salario'].astype(float)
    return df

# Leitura do CSV
df = pd.read_csv('seu_arquivo.csv')  # substitua pelo caminho real
df = limpar_dados(df)

# Separação por sexo
salarios_homens = df[df['Sexo'] == 'Masculino']['Salario']
salarios_mulheres = df[df['Sexo'] == 'Feminino']['Salario']

# Estatísticas
print("Qtd Homens:", len(salarios_homens))
print("Qtd Mulheres:", len(salarios_mulheres))

print("Dispersão Homens:", [
    salarios_homens.var(),
    salarios_homens.std(),
    salarios_homens.max() - salarios_homens.min()
])

print("Dispersão Mulheres:", [
    salarios_mulheres.var(),
    salarios_mulheres.std(),
    salarios_mulheres.max() - salarios_mulheres.min()
])

