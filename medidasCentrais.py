import numpy as np

medidas = ['Média', 'Mediana', 'Moda']
homens = [media_homens, mediana_homens, moda_homens]
mulheres = [media_mulheres, mediana_mulheres, moda_mulheres]

x = np.arange(len(medidas))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, homens, width, label='Homens')
ax.bar(x + width/2, mulheres, width, label='Mulheres')

ax.set_ylabel('Salário (R$)')
ax.set_title('Medidas de Tendência Central por Gênero')
ax.set_xticks(x)
ax.set_xticklabels(medidas)
ax.legend()

plt.savefig('medidas_centrais.png')
