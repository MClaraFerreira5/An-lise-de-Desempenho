# 1. Média aritmética
def media_aritmetica(lista): return sum(lista) / len(lista)

# 2. Fatorial [recursão]
def fatorial(n):
    if n == 0: return 1
    return n * fatorial(n - 1)

# 3. Contar palavras
def contar_palavras(s): return len(s.split())

# 4. Soma de todos os elementos (Matriz)
def soma_matriz(m): return sum(sum(linha) for linha in m)

# 5. Segundo maior elemento
def segundo_maior(lista):
    maior = segundo = float('-inf')
    for n in lista:
        if n > maior: segundo, maior = maior, n
        elif n > segundo and n != maior: segundo = n
    return segundo

# 6. Soma dos dígitos [recursão]
def soma_digitos(n):
    if n == 0: return 0
    return (n % 10) + soma_digitos(n // 10)

# 7. Verificar anagrama
def eh_anagrama(s1, s2):
    t = lambda s: sorted(s.lower().replace(" ", ""))
    return t(s1) == t(s2)

# 8. Maior elemento da matriz
def maior_matriz(m): return max(max(linha) for linha in m)

# 9. Mover zeros para o final
def mover_zeros(lista):
    nz = [x for x in lista if x != 0]
    return nz + [0] * (len(lista) - len(nz))

# 10. Potência inteira [recursão]
def potencia(b, e):
    if e == 0: return 1
    return b * potencia(b, e - 1)

# 11. Inverter palavras
def inverter_palavras(s): return " ".join(s.split()[::-1])

# 12. Soma da diagonal principal
def soma_diagonal(m): return sum(m[i][i] for i in range(len(m)))

# 13. Par com soma alvo
def tem_soma_alvo(lista, x):
    vistos = set()
    for n in lista:
        if x - n in vistos: return True
        vistos.add(n)
    return False

# 14. Contar dígitos [recursão]
def contar_digitos(n):
    if n < 10: return 1
    return 1 + contar_digitos(n // 10)

# 15. Palavras repetidas
def palavras_repetidas(s):
    p = s.lower().split()
    return len([x for x in set(p) if p.count(x) > 1])

# 16. Verificar matriz simétrica
def eh_simetrica(m):
    return all(m[i][j] == m[j][i] for i in range(len(m)) for j in range(len(m)))

# 17. Remover duplicatas
def remover_duplicatas(lista):
    res = []
    for x in lista:
        if x not in res: res.append(x)
    return res

# 18. Soma de 1 até n [recursão]
def soma_ate_n(n):
    if n == 1: return 1
    return n + soma_ate_n(n - 1)

# 19. Linha com maior soma
def indice_maior_linha(m):
    somas = [sum(l) for l in m]
    return somas.index(max(somas))

# 20. Compressão simples
def compressao_simples(s):
    if not s: return ""
    r, c = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]: c += 1
        else:
            r.append(s[i-1] + str(c)); c = 1
    r.append(s[-1] + str(c))
    f = "".join(r)
    return f if len(f) < len(s) else s

# 21. Rotacionar lista
def rotacionar(lista, k):
    k %= len(lista)
    return lista[-k:] + lista[:-k]

# 22. Extrair dígitos de string
def extrair_digitos(s): return "".join([c for c in s if c.isdigit()])

# 23. Soma das bordas
def soma_bordas(m):
    l, c = len(m), len(m[0])
    s = sum(m[0]) + sum(m[-1])
    for i in range(1, l - 1): s += m[i][0] + m[i][-1]
    return s

# 24. Inverter string [recursão]
def inverter_str_rec(s):
    if len(s) <= 1: return s
    return s[-1] + inverter_str_rec(s[:-1])

# 25. Interseção de listas
def intersecao(a, b): return list(set(a) & set(b))

# 26. Maior prefixo comum
def prefixo_comum(s1, s2):
    res = ""
    for c1, c2 in zip(s1, s2):
        if c1 == c2: res += c1
        else: break
    return res

# 27. Contar pares na matriz
def contar_pares_matriz(m):
    return sum(1 for linha in m for x in linha if x % 2 == 0)

# 28. Verificar string numérica
def eh_numerica(s): return s.isdigit()

# 29. Multiplicação por escalar
def escalar_matriz(m, k): return [[x * k for x in linha] for linha in m]

# 30. Elemento majoritário
def majoritario(lista):
    for x in set(lista):
        if lista.count(x) > len(lista) // 2: return x
