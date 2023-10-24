import pandas as pd
import matplotlib as plt
import numpy as np


def menu():
    while True:
        print("                      ")
        print("=========MENU==============")
        print("1: Adicionar um funcionário")
        print("2: Calcular IR")
        print("3: Imprimir relatório")
        print("4: Sair\n")
        escolha = input("Escolha uma das opções:")
        if escolha == '1':
            cadastros_instance.ler_dados()
        elif escolha == '2':
            cadastros_instance.calculo_ir()
        elif escolha == '3':
            cadastros_instance.imprimir_relatorio()
        elif escolha == '4':
            break
        else:
            print("Escolha inválida, tente novamente")


class Funcionario:
    def __init__ (self,nome,cargo,salario,horas):
        self.nome = nome
        self.cargo = cargo
        self.horas = horas
        self.salario = salario

class cadastros:
    def __init__ (self):
        self.funcionarios = []
        self.descontos_ir = 0
        self.total_salario_bruto = 0
        self.total_salario_liquido = 0
    



    def ler_dados(self):
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo do funcionário: ")
            salario = float(input("Salário do funcionário: "))
            horas = float(input("Horas trabalhadas do funcionário: "))
            funcionario = Funcionario(nome, cargo, salario, horas)
            self.funcionarios.append(funcionario)

    def calculo_ir(self):
        for funcionario in self.funcionarios:
            salario = funcionario.salario
            if salario <= 1500.0:
                desconto = 0
            elif 1500 < salario <= 3000:
                desconto = salario * 0.15
            elif 3000 < salario <= 5000:
                desconto = salario * 0.20
            elif 5000 < salario:
                desconto = salario * 0.27
            funcionario.desconto_ir = desconto
            funcionario.salario_liquido = salario - desconto
            self.descontos_ir += desconto
            self.total_salario_bruto += salario
            self.total_salario_liquido += funcionario.salario_liquido
        print("Concluido")


    def imprimir_relatorio(self):
            df = pd.DataFrame([(f.nome, f.cargo, f.salario, f.horas, f.desconto_ir, f.salario_liquido)
                            for f in self.funcionarios],
                            columns=["Nome", "Cargo", "Salário", "Horas Trabalhadas", "Desconto IR", "Salário Líquido"])
            print(df)

            print(f"Total de descontos de IR: {self.descontos_ir}")
            print(f"Total de salário bruto: {self.total_salario_bruto}")
            print(f"Total de salário líquido: {self.total_salario_liquido}")

cadastros_instance = cadastros()
if __name__ == "__main__":
    menu()