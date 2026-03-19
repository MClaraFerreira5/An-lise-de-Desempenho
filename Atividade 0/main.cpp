#include <iostream>
#include <vector>
#include <limits>

void encontrarPrimos(int n) {
    std::vector<bool> ehPrimo(n + 1, true);

    if (n >= 0) ehPrimo[0] = false;
    if (n >= 1) ehPrimo[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (ehPrimo[p]) {
            for (int i = p * p; i <= n; i += p) {
                ehPrimo[i] = false;
            }
        }
    }

    std::vector<int> primosEncontrados;
    for (int p = 2; p <= n; p++) {
        if (ehPrimo[p]) {
            primosEncontrados.push_back(p);
        }
    }
    std::cout << "\nO valor de N: " << n << "\n";
    std::cout << "Os numeros primos encontrados: ";

    for (size_t i = 0; i < primosEncontrados.size(); ++i) {
        std::cout << primosEncontrados[i];
        if (i < primosEncontrados.size() - 1) {
            std::cout << " - ";
        }
    }

    std::cout << "\nA quantidade de numeros primos encontrados: " << primosEncontrados.size() << "\n\n";
}

int main() {
    int n;

    while (true) {
        std::cout << "Digite um numero inteiro N (maior que 0): ";

        if (std::cin >> n && n > 0) {
            break;
        } else {
            std::cout << "Erro: Entrada invalida. Por favor, digite um numero inteiro positivo.\n\n";

            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

    encontrarPrimos(n);

    return 0;
}
