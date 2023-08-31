# Função para calcular salário
def calcular_salario(salario_hora, horas_trabalhadas):
    return salario_hora * horas_trabalhadas

# Função para exibir os cálculos com três números
def exibir_resultados(a, b, c):
    print("\nCálculos com os três números informados:")
    print("1) Produto do dobro do primeiro com metade do segundo:", 2 * a * (b / 2))
    print("2) Soma do triplo do primeiro com o terceiro:", 3 * a + c)
    print("3) Terceiro elevado ao cubo:", c ** 3)

# Função para retornar os cálculos com três números
def retornar_resultados(a, b, c):
    return (2 * a * (b / 2), 3 * a + c, c ** 3)

# Função para verificar se um ano é bissexto
def ano_bissexto(ano):
    # Verifica as regras de anos bissextos sem usar condicionais
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

# Função principal
def main():
    # Solicita informações de salário
    salario_hora = float(input("Informe o salário por hora: "))
    horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
    print("\nSalário a ser recebido:", calcular_salario(salario_hora, horas_trabalhadas))

    # Solicita três números
    a = float(input("\nInforme o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    c = float(input("Informe o terceiro número: "))
    
    # Exibe e retorna os cálculos com os três números
    exibir_resultados(a, b, c)
    res1, res2, res3 = retornar_resultados(a, b, c)
    print("\nRetornando os resultados:")
    print("1) ", res1)
    print("2) ", res2)
    print("3) ", res3)

    # Solicita um ano e verifica se é bissexto
    ano = int(input("\nInforme um ano para verificar se é bissexto: "))
    print(ano, "é bissexto?" , ano_bissexto(ano))

# Executa a função principal
main()

