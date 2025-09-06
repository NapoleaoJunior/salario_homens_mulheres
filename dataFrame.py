import pandas as pd

df = pd.read_excel(r"C:\Users\junio\OneDrive\Área de Trabalho\Ciencia de dados\salario_homens_mulheres\dataset_salarios.xlsx")





homens = df[df['Sexo'] == 'Masculino']
media_h = homens['Salario'].mean()
print(f"Média salarial dos homens: {media_h:.2f}")

# Carregar a planilha
df = pd.read_excel("dataset_salario.xlsx")
df['Sexo'] = df['Sexo'].str.strip().str.capitalize()


# Separar os grupos
homens = df[df['Sexo'] == 'Homem']
mulheres = df[df['Sexo'] == 'Mulher']

# Função para medidas de dispersão
def dispersao(grupo):
    return {
        'Variância': grupo['Salario'].var(),
        'Desvio Padrão': grupo['Salario'].std(),
        'Amplitude': grupo['Salario'].max() - grupo['Salario'].min()
    }
    
    


# Exibir os resultados
print("Dispersão Homens:", dispersao(homens))
print("Dispersão Mulheres:", dispersao(mulheres))
print("Valores únicos na coluna Sexo:", df['Sexo'].unique())
print("Quantidade de homens:", len(homens))
print("Quantidade de mulheres:", len(mulheres))
print("Salários dos homens:", homens['Salario'].head())
print("Salários das mulheres:", mulheres['Salario'].head())
