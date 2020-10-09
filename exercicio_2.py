def cria_matriz(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + '] '))
            linha.append(valor)
        matriz.append(linha)

    print(matriz)
    return matriz

def le_matriz():
    lin = int(input('Digite numero de linhas da matriz: '))
    col = int(input('Digite o numero de colunas da matriz: '))
    return cria_matriz(lin, col)

def somar(a, b):
    matriz = []
    linhas_a, linhas_b = len(a), len(b)
    colunas_a, colunas_b = len(a[0]), len(b[0])
    if (linhas_a == linhas_b) and (colunas_a == colunas_b):
        for i in range(linhas_a):
            linha = [0]*colunas_a
            matriz.append(linha)
            for j in range(colunas_a):
                matriz[i][j] = a[i][j] + b[i][j]
    else:
        print("valores da colunas e/ou linhas nao batem")
    return matriz

def subtrair(a, b):
    matriz = []
    linhas_a, linhas_b = len(a), len(b)
    colunas_a, colunas_b = len(a[0]), len(b[0])
    if (linhas_a == linhas_b) and (colunas_a == colunas_b):
        for i in range(linhas_a):
            linha = [0]*colunas_a
            matriz.append(linha)
            for j in range(colunas_a):
                matriz[i][j] = a[i][j] - b[i][j]
    else:
        print("valores da colunas e/ou linhas nao batem")
    return matriz

def multiplicar(a, b):
    linhas_A, colunas_A = len(a), len(a[0])
    linhas_B, colunas_B = len(b), len(b[0])
    matriz = []
    if colunas_A == linhas_B:
        assert colunas_A == linhas_B
        for linha in range(linhas_A):
            matriz.append([])
            for coluna in range(colunas_B):
                matriz[linha].append(0)
                for m in range(colunas_A):
                    matriz[linha][coluna] += a[linha][m] * b[m][coluna]
    else:
        print('numero de colunas da primeira matriz deve ser igual ao numero de linhas ')
    return matriz

def det(matriz, ordem):

    if ordem == 1:
        determinante = matriz[0][0]
        return determinante

    elif ordem == 2:
        principal, secundaria = 1, 1
        for i in range(ordem):
            for j in range(ordem):
                if i == j:
                    principal *= matriz[i][j]
                else:
                    secundaria *= matriz[i][j]
        determinante = principal - secundaria
        return determinante

    elif ordem == 3:
        a, b, c = matriz[0]
        efhi = [x[1:] for x in matriz[1:]]
        dfgi = [x[::2] for x in matriz[1:]]
        degh = [x[0:2] for x in matriz[1:]]
        det = (a * det2x2(efhi) - b * det2x2(dfgi) + c * det2x2(degh))

        return det

    else:
        print('determinante nao e de ordem 1, 2 ou 3')

def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def transpose(c):
    return [[row[col] for row in c] for col in range(len(c[0]))]

# resultado = det(le_matriz(), 3)
# print(resultado)

A = le_matriz()
B = le_matriz()
T = transpose(A)
soma = somar(B, T)
resultado = multiplicar(A, soma)
print(resultado)
