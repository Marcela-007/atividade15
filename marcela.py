# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
med1 = float(input("Insira a primeira medida: "))
med2 = float(input("Insira a segunda medida: "))
med3 = float(input("Insira a terceira medida: "))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print("É um triÂngulo")
else:
    print("Não é um triângulo")