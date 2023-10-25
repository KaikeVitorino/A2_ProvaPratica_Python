import matplotlib.pyplot as plt
import numpy as np

class Armazem:
    def __init__(self):
        self.quantidade_vendidas = {}
        self.precos = {}

    def menu_principal(self):
        while True:
            print("\nMenu Principal:")
            print("1. Registrar venda")
            print("2. Calcular faturamento")
            print("3. Exibir percentuais de vendas")
            print("4. Gravar dados das vendas em arquivo")
            print("5. Imprimir gráfico das 5 mercadorias mais vendidas")
            print("6. Sair")

            opcao = int(input("Escolha uma opcao: "))

            if opcao == 1:
                self.registrar_venda()
            elif opcao == 2:
                self.calcular_faturamento()
            elif opcao == 3:
                self.exibir_percentuais_vendas()
            elif opcao == 4:
                self.gravar_dados_em_arquivo()
            elif opcao == 5:
                self.imprimir_grafico()
            elif opcao == 6:
                break
            else:
                print("Opcao invalida!")

    def registrar_venda(self):
        while True:
            try:
                mercadoria = int(input("Informe o numero da mercadoria (1 a 100): "))
                quantidade = int(input("Informe a quantidade vendida: "))
                preco = float(input("Informe o preço da mercadoria: "))

                if 1 <= mercadoria <= 100:
                    if mercadoria in self.quantidade_vendidas:
                        self.quantidade_vendidas[mercadoria] += quantidade
                    else:
                        self.quantidade_vendidas[mercadoria] = quantidade

                    self.precos[mercadoria] = preco
                    break
                else:
                    print("Numero de mercadoria invalido.")
            except ValueError:
                print("Digite um número inteiro válido.")

    def calcular_faturamento(self):
        faturamento_total = 0
        for mercadoria, quantidade in self.quantidade_vendidas.items():
            if mercadoria in self.precos:
                preco = self.precos[mercadoria]
                faturamento = quantidade * preco
                faturamento_total += faturamento
                print(f"Mercadoria {mercadoria}: Quantidade vendida = {quantidade}, Preco unitario = {preco}, Faturamento = {faturamento}")

        print(f"Faturamento total: {faturamento_total}")

    def exibir_percentuais_vendas(self):
        faturamento_total = sum(self.quantidade_vendidas[mercadoria] * self.precos[mercadoria] for mercadoria in self.quantidade_vendidas)
        for mercadoria, quantidade in self.quantidade_vendidas.items():
            if mercadoria in self.precos:
                preco = self.precos[mercadoria]
                faturamento = quantidade * preco
                percentual = (faturamento / faturamento_total) * 100
                print(f"Mercadoria {mercadoria}: Percentual de vendas = {percentual:.2f}%")

    def gravar_dados_em_arquivo(self):
        with open("dados_vendas.txt", "w") as arquivo:
            arquivo.write("Mercadoria, Quantidade vendida, Preco unitario, Faturamento\n")
            for mercadoria, quantidade in self.quantidade_vendidas.items():
                if mercadoria in self.precos:
                    preco = self.precos[mercadoria]
                    faturamento = quantidade * preco
                    arquivo.write(f"{mercadoria}, {quantidade}, {preco}, {faturamento}\n")

        print("Dados das vendas gravados em arquivo.")

    def imprimir_grafico(self):
        top5_mercadorias = sorted(self.quantidade_vendidas.items(), key=lambda x: x[1], reverse=True)[:5]
        mercadorias = [str(item[0]) for item in top5_mercadorias]
        quantidades = [item[1] for item in top5_mercadorias]

        plt.figure(figsize=(10, 6))
        plt.bar(mercadorias, quantidades, color='skyblue')
        plt.xlabel('Mercadorias')
        plt.ylabel('Quantidade Vendida')
        plt.title('Top 5 Mercadorias Mais Vendidas')
        plt.show()
