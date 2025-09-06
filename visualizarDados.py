import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r"C:\Users\junio\OneDrive\Área de Trabalho\Ciencia de dados\salario_homens_mulheres\dataset_salarios.xlsx")


# Boxplot comparativo
sns.boxplot(x='Sexo', y='Salario', data=df)
plt.title("Distribuição Salarial por Sexo")
plt.show()
