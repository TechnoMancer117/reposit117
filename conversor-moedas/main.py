def converter_moeda(valor, taxa_cambio):
  return valor * taxa_cambio

# Exemplo de uso
valor = float(input("Digite o valor em reais: "))
taxa = float(input("Digite a taxa de câmbio (ex: dólar): "))
convertido = converter_moeda(valor, taxa)
print(f"Valor convertido: {convertido:.2f}")