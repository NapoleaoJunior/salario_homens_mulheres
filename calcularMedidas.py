# Separar os grupos
homens = df[df['Sexo'] == 'Homem']
mulheres = df[df['Sexo'] == 'Mulher']

# Função para calcular medidas de tendência central
def tendencia_central(grupo):
    return {
        'Média': grupo['Salario'].mean(),
        'Mediana': grupo['Salario'].median(),
        'Moda': grupo['Salario'].mode()[0] if not grupo['Salario'].mode().empty else None
    }

print("Homens:", tendencia_central(homens))
print("Mulheres:", tendencia_central(mulheres))
