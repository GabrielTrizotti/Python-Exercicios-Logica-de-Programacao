# Entrada de dados (Declaração das variáveis com a entrada de seus respectivos valores")
precoOriginal = float( input("Insira o valor original: R$"))
valorPorcentagem = float( input("Insira a porcentagem a ser adicionada: "))

# Cálculo
calculoPorcentagem = valorPorcentagem / 100
aumento = precoOriginal * calculoPorcentagem
precoFinal = precoOriginal + aumento

# Resultado dos cálculos (Saída de dados)
print("Valor original: R$",precoOriginal)
print("Aumento: R$",aumento)
print("Preço final: R$",precoFinal)
