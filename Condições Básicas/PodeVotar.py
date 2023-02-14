# Declaração de variáveis
ano_nasci = int( input("Insira o seu ano de nascimento: "))
ano_atual = int( input("Insira o ano atual: "))

# Cálculo
idade = ano_atual - ano_nasci 

# Condição
if idade >= 18:
  print("Você pode votar com", idade,"anos de idade.")
else:
  print("Você não pode votar com", idade,"anos de idade.")
