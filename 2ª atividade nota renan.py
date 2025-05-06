
'''#algoritmo para exibir numeros pares com excessões
for numero in range(0,31,2): # itera de 0 a 30 com passo de 2(numeros pares)
    if numero in [10,20,30]: # verifica se o número esta na lista de exclusão
        continue # pula para a proxima iteração, ignorando o numero
    print(numero) # exibe o numero
'''
              
    # solicita as duas notas
nota1 = float(input("digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("digite a primeira nota: "))

nota2 = input("digite a segunda nota")

    # calcular a média aritmética 
media = (nota1 + nota2) / 2
    # exibe a media e o resultado final
print(f"\nA media do aluno é: {media:.2f}") # Mostra a media com duas casas decimais
if media >= 6:
    