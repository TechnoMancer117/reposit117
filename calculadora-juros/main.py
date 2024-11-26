# Calculadora de Juros Compostos
def calcular_juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa / 100) ** tempo
    return montante

# Exemplo de uso
capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de juros (%): "))
tempo = int(input("Digite o tempo (em meses): "))

montante = calcular_juros_compostos(capital, taxa, tempo)
print(f"Montante final: R$ {montante:.2f}")