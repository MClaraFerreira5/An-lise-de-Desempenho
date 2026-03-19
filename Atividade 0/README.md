# Atividade 0: Contador de Números Primos (C++)

Programa que recebe um número `N` e retorna a quantidade e a lista de números primos no intervalo de 1 até `N`. 

## ⚡ Análise de Desempenho
Para evitar a lentidão da força bruta, o algoritmo implementado é o **Crivo de Eratóstenes**:
* **Complexidade de Tempo:** `O(N log(log N))` - Altamente eficiente para valores grandes.
* **Complexidade de Espaço:** `O(N)` - Uso de memória otimizado através de `std::vector<bool>`.

## 🛡️ Funcionalidades
* **Tratamento de Erros:** O programa não quebra se o usuário digitar letras, palavras ou números menores que 1.
* **Saída Formatada:** Exibe os primos separados exatamente por hífen (`-`).

## 🚀 Como Executar

Abra o terminal na pasta do arquivo e rode os comandos:

**1. Compilar:**
```bash
g++ main.cpp -o primos