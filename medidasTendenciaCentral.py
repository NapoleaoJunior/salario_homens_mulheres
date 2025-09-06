import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Calcular medidas
media_h = homens['Salario'].mean()
mediana_h = homens['Salario'].median()
moda_h = homens['Salario'].mode()[0]

media_m = mulheres['Salario'].mean()
mediana_m = mulheres['Salario'].median()
moda_m = mulheres['Salario'].mode()[0]

# Criar DataFrame para gráfico
tendencia_df = pd.DataFrame({
    'Homens': [media_h, mediana_h, moda_h],
    'Mulheres': [media_m, mediana_m, moda_m]
}, index=['Média', 'Mediana', 'Moda'])

# Plotar
tendencia_df.plot(kind='bar', figsize=(8,5), title='Medidas de Tendência Central')
plt.ylabel('Salário')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
