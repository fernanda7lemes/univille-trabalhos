import numpy as np

#exercício 10
notas = np.zeros(15)
soma = 0
for i in range(15):
    notas[i] = float(input("Digite a nota: "))
    soma += notas[i]

print(f"A média geral é {soma/15}")


#exercício 11
vetor = np.zeros(10)
negativos = 0
soma = 0

for i in range(10):
    vetor[i] = float(input("Digite um número: "))
    if vetor[i] < 0:
        negativos += 1
    else:
        soma += vetor[i]

print(f'A quantidade de números negativos é de {negativos} e a soma dos positivos é {soma}')


#exercício 12

def ler_vetor(tamanho):
    vetor = np.zeros(tamanho, dtype=int) 
    print(f"Digite {tamanho} números inteiros:")
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Elemento {i+1}: "))
                vetor[i] = numero
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return vetor

def imprimir_vetor(vetor):
    print("Vetor:", vetor)

def inverter_vetor(vetor):
    return vetor[::-1] 

def main():
    TAMANHO_VETOR = 20
    
    vetor = ler_vetor(TAMANHO_VETOR)
    
    print("Vetor original:")
    imprimir_vetor(vetor)

    vetor_invertido = inverter_vetor(vetor)
    
    print("Vetor modificado:")
    imprimir_vetor(vetor_invertido)

if __name__ == "__main__":
    main()


#exercício 13

candidatos = int(input("Digite o número de candidatos: "))
votantes = int(input("Digite o número de votantes: "))

votos = np.zeros(candidatos)

for i in range(votantes):
    voto = int(input(f'Digite o número do candidato (1 a {candidatos}): '))
    if 1 <= voto <= candidatos:
        votos[voto - 1] += 1
    else:
        print("Voto inválido.")

for i in range(candidatos):
    print(f'Candidato {i+1}: {votos[i]} votos.')


#exercício 14

total_matriculas = 100

matriculas = np.zeros(total_matriculas, dtype=int)

for i in range(total_matriculas):
    while True:
        try:
            matricula = int(input(f"Digite a matrícula {i + 1}: "))
            if matricula in matriculas:
                print("Erro: Matrícula já cadastrada! Insira um número diferente.")
            else:
                matriculas[i] = matricula
                break
        except ValueError:
            print("Erro: Insira um número válido de matrícula.")

print("\nMatrículas cadastradas:")
print(matriculas)


#exercício 15

n = int(input("Digite o número de elementos no vetor: "))

vetor = np.array([int(input("Digite um valor inteiro: ")) for _ in range(n)])

pares = vetor[vetor % 2 == 0]
impares = vetor[vetor % 2 != 0]

print("Valores pares:", pares)
print("Valores ímpares:", impares)


#exercício 16

def ler_vetor(nome, tamanho):
    """ Função para ler um vetor de números inteiros """
    vetor = np.zeros(tamanho, dtype=int)
    print(f"Digite os {tamanho} elementos do vetor {nome} (em ordem crescente):")
    for i in range(tamanho):
        while True:
            try:
                elemento = int(input())
                vetor[i] = elemento
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return vetor

def intercala_vetores(A, B):
    """ Função para intercalação de dois vetores ordenados """
    N = len(A)
    M = len(B)
    C = np.zeros(N + M, dtype=int)
    i, j, k = 0, 0, 0

    while i < N and j < M:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < N:
        C[k] = A[i]
        i += 1
        k += 1

    while j < M:
        C[k] = B[j]
        j += 1
        k += 1

    return C

def main():
    N = int(input("Digite o número de elementos do vetor A: "))
    M = int(input("Digite o número de elementos do vetor B: "))

    A = ler_vetor("A", N)
    B = ler_vetor("B", M)

    C = intercala_vetores(A, B)

    print("Vetor C intercalação:", C)

if __name__ == "__main__":
    main()


#exercício 17

notas = np.array([9.9, 9.7, 9.8, 10, 10])

notas_filtradas = np.delete(notas, [np.argmax(notas), np.argmin(notas)])

media_final = np.mean(notas_filtradas)

print(f'A média final do quesito é: {media_final:.2f}')