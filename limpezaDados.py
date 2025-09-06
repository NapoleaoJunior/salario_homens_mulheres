import pandas as pd

def limpar_dados(df):
    # Padroniza a coluna 'Sexo'
    df['Sexo'] = df['Sexo'].str.strip().str.lower()

    # Converte para formato padronizado
    df['Sexo'] = df['Sexo'].replace({
        'masculino': 'Masculino',
        'feminino': 'Feminino'
    })

    # Remove linhas com sexo inválido ou salário nulo
    df = df[df['Sexo'].isin(['Masculino', 'Feminino'])]
    df = df[pd.to_numeric(df['Salario'], errors='coerce').notnull()]

    # Converte salário para float
    df['Salario'] = df['Salario'].astype(float)

    return df

