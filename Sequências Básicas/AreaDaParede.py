# Entrada de dados (Declaração das variáveis com a entrada de seus respectivos valores")
altura = float( input("Insira a altura: "))
largura = float( input("Insira a largura: "))
renda = float( input("Insira a renda em metro da tinta por litro: "))

# Cálculo para descobrir a área da parede
area = altura * largura 

# Cálculo para descobrir a quantidade de tinta necessária
tinta = area / renda

# Resultado dos cálculos
print("A área da parede é de", area,"metros quadrados.")
print("Serão necessários", tinta,"Litros de tinta.")
