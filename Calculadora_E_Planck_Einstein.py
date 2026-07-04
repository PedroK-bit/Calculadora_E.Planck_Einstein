from art import text2art as t2
import math

TEMA = "E.Planck-Einstein"
ART = t2(TEMA)
print(ART)

def calcular():
    #CALCULADORA
    #Formula: E = h.f
    F = float(input("Digite um valor de frequência: "))
    H = 6.62 * 10 ** -34

    E = H * F
    print(f"Energia é {E:.2e} J")

calcular()

perg = input("Deseja um breve explicação sobre tamanhos de ENERGIA?: ")
if perg == "s":
    print("Quanto mais negativo o expoente na notação cientifica, menor o valor da energia\n" \
    "Exemplos: 10^-34 = muito baixa\n" \
    "10^0 = média\n" \
    "10^34 = muito alta")
           
else:
    print("\n❌ ENCERRADO ❌\n")


