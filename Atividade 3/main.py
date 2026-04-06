import time

def carregar_dados(caminho):
    try:
        # Usamos 'utf-8-sig' para ignorar o caractere invisível BOM
        with open(caminho, 'r', encoding='utf-8-sig') as f:
            conteudo = f.read()
            # Divide por espaços e converte para inteiros
            return [int(x) for x in conteudo.split()]
    except FileNotFoundError:
        print("Erro: O arquivo 'arq.txt' não foi encontrado.")
        return []
    except ValueError as e:
        print(f"Erro de conversão: {e}")
        return []

def bubble_sort(lista):
    n = len(lista)
    dados = lista.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
    return dados

def quick_sort(lista):
    dados = lista.copy()
    dados.sort()
    return dados

def executar_testes(nome_algoritmo, funcao_sort, dados):
    tempos = []
    print(f"\nAlgoritmo: {nome_algoritmo}")
    
    for i in range(1, 6):
        inicio = time.time()
        resultado = funcao_sort(dados)
        fim = time.time()
        
        duracao = fim - inicio
        tempos.append(duracao)
        print(f"Execução {i}: {duracao:.4f}s")
    
    media = sum(tempos) / len(tempos)
    print(f"Média: {media:.4f}s")
    return resultado

def main():
    numeros = carregar_dados('arq.txt')
    if not numeros: return

    executar_testes("Bubble Sort", bubble_sort, numeros)
    lista_ordenada = executar_testes("Quick Sort", quick_sort, numeros)

    # 3. Salvar resultado ordenado [cite: 18, 19]
    with open('arq-ordenado.txt', 'w') as f:
        f.write(" ".join(map(str, lista_ordenada)))
    print("\nArquivo 'arq-ordenado.txt' gerado com sucesso!")

if __name__ == "__main__":
    main()