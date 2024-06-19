#le aventuras#
import csv

def ler_aventuras_csv(arquivo):
    vetor = []
    with open(arquivo, 'r') as sei_la:
        minha_vida = csv.DictReader(sei_la)
        for n in minha_vida:

            vetor.append(n)
    return vetor

arquivo = 'trabalho.csv'
aventuras = ler_aventuras_csv(arquivo)
print(aventuras)

def esperar_para_continuar():
    continuar = input("Digite C para continuar: ")
    while continuar != 'c' and continuar != 'C':
        continuar = input("Digite C para continuar: ")

esperar_para_continuar()

def mostrar_aventura_especifica(vetor, indice):
  if indice >= 0 and indice <= 40: 
      print("Aventura", indice, ":", vetor[indice])
  else:
      print("Número de aventura inválido!")

indice_aventura = int(input("Digite o índice de uma aventura (0 a 40): "))
mostrar_aventura_especifica(aventuras, indice_aventura)

def remover_aventura(vetor, indice):
  total_aventuras = 40  
  if indice >= 0 and indice <= total_aventuras:
      vetor.pop(indice)
      print("Aventura removida")
  else:
      print("Número inválido")
      indice_aventura = int(input("Digite o índice de uma aventura (0 a 40): "))
  return vetor 

remove = remover_aventura(aventuras, indice_aventura)
print(remove)