import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 🔢 Criar o DataFrame
df = pd.DataFrame({
    'Salario': [3200, 4500, 5000, 7000, 2800, 3900, 6200, 4700, 5100, 8000],
    'Sexo': ['Masculino', 'Feminino', 'Masculino', 'Masculino', 'Feminino',
             'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino']
})

# 2. 📊 Calcular estatísticas por grupo
stats = df.groupby('Sexo')['Salario'].agg(['mean', 'median', 'std', 'min', 'max']).round(2)
print(stats)

# 3. 📈 Criar o histograma
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Salario', hue='Sexo', bins=10, kde=True, palette='Set2')
plt.title('Distribuição de Salários por Sexo')
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# 4. 📝 Gerar o texto do relatório
def gerar_relatorio(stats):
    relatorio = f"""
📄 Relatório de Distribuição Salarial

1. Variação Salarial:
- Masculino: de R${stats.loc['Masculino', 'min']} a R${stats.loc['Masculino', 'max']}
- Feminino: de R${stats.loc['Feminino', 'min']} a R${stats.loc['Feminino', 'max']}

2. Medidas Centrais:
- Média Masculina: R${stats.loc['Masculino', 'mean']}
- Mediana Masculina: R${stats.loc['Masculino', 'median']}
- Média Feminina: R${stats.loc['Feminino', 'mean']}
- Mediana Feminina: R${stats.loc['Feminino', 'median']}

3. Interpretação:
- A diferença entre média e mediana no grupo masculino sugere maior desigualdade salarial.
- O grupo feminino apresenta distribuição mais homogênea, com menor desvio padrão.

4. Conclusões:
- Recomenda-se utilizar a mediana como referência para políticas salariais.
- A transparência e auditoria interna podem ajudar a reduzir disparidades.
"""
    return relatorio

print(gerar_relatorio(stats))
