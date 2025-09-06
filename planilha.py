import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Carrega os dados
df = pd.read_excel(r"C:\Users\junio\OneDrive\Área de Trabalho\Ciencia de dados\salario_homens_mulheres\dataset_salarios.xlsx")

df = limpar_dados(df)

# Exibe o DataFrame
print(df)

# Gráfico de dispersão (boxplot)
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.boxplot(x='Sexo', y='Salario', data=df, palette='pastel')
plt.title('Distribuição Salarial por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Salário')
plt.tight_layout()
plt.show()

# Gráfico de média salarial por sexo
media_por_sexo = df.groupby('Sexo')['Salario'].mean().reset_index()
plt.figure(figsize=(6, 4))
sns.barplot(x='Sexo', y='Salario', data=media_por_sexo, palette='muted')
plt.title('Média Salarial por Sexo')
plt.ylabel('Salário Médio')
plt.tight_layout()
plt.show()

# Estilo do gráfico
sns.set_style("whitegrid")

# Histograma dos salários
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Salario', bins=20, kde=True, color='skyblue')

plt.title('Distribuição de Salários')
plt.xlabel('Faixa Salarial (R$)')
plt.ylabel('Número de Pessoas')
plt.tight_layout()
plt.show()
