def dispersao(grupo):
    return {
        'Variância': grupo['Salario'].var(),
        'Desvio Padrão': grupo['Salario'].std(),
        'Amplitude': grupo['Salario'].max() - grupo['Salario'].min()
    }

print("Dispersão Homens:", dispersao(homens))
print("Dispersão Mulheres:", dispersao(mulheres))
