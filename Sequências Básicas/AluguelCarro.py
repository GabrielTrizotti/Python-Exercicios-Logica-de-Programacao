# Entrada de dados (Declaração das variáveis com a entrada de seus respectivos valores")
dias = float( input("Insira a quantidade de dias alugados: "))
km = float( input("Insira a quantidade de quilômetros percorridos: "))

# Cálculo para saber o valor total da locação
valorDias =  dias * 90
valorKm = km * 1
total = valorDias + valorKm

# Exibição dos resultados (Saída de dados)
print("Valor a pagar pelos dias percorridos: R$",valorDias)
print("Valor a pagar por quilômetros rodados: R$",valorKm)
print("Total a pagar: R$",total)
