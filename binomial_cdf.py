from scipy.stats import binom

def calculate_probability(n, p, k):
    # Calcula a probabilidade de no máximo k 
    prob = binom.cdf(k, n, p)
    return prob * 100  # Converte para porcentagem

def main():     
    while True:
        print("\n---Probabilidade binomial C.D.F---\n")
        n = int(input("Digite um inteiro para a amostra: ")) 
        p = float(input("Digite o valor de sucesso da probabilidade(decimal-ex:0.23):"))

        while True:

            print("\nEscolha uma opção:")
            print("1. Calcular probabilidade de no máximo k ")
            print("2. Calcular probabilidade de pelo menos k ")
            print("3. Calcular probabilidade de exatamente k ")
            print("4. Redefinir população e probabilidade")
            print("5. Sair")
            choice = int(input("Digite sua escolha: "))

            if choice == 1:
                k = int(input("Digite o valor de k: "))
                prob = calculate_probability(n, p, k)
                print(f"A probabilidade de no máximo {k} é {prob:.2f}%")
            elif choice == 2:
                k = int(input("Digite o valor de k: "))
                prob = 1 - binom.cdf(k-1, n, p)
                print(f"A probabilidade de pelo menos {k} é {prob:.2f}%")
            elif choice == 3:
                k = int(input("Digite o valor de k: "))
                prob = binom.pmf(k, n, p)
                print(f"A probabilidade de exatamente {k} é {prob:.2f}%")
            elif choice == 4:
                print("Redefinindo amostra e população.")
                break
            elif choice == 5:
                print("Encerrando o programa.")
                return
            else:
                print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
