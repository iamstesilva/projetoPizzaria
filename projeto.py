import time
import os
os.system('cls')

RESET = '\033[m'
VERDE = '\033[1;32m'
AZUL = '\033[1;34m'
AMARELO = '\033[1;33m'
VERMELHO = '\033[1;31m'
CINZA = '\033[1;90m'
BRANCO = '\033[1;97m'
MAGENTA = '\033[1;35m'
BRANCO_NEGRITO = '\033[1;97m'

print(f"{VERDE}BEM-VINDO A PIZZARIA 2° DS!{RESET}\n".center(80))
time.sleep(2)

class Pizzaria:
    def __init__(self):
        self.menu_pizzas = {
            "1": {"nome": "Margherita", "preco": 25.00},
            "2": {"nome": "Pepperoni", "preco": 30.00},
            "3": {"nome": "Quatro Queijos", "preco": 35.00},
            "4": {"nome": "Vegetariana", "preco": 28.00},
            "5": {"nome": "Calabresa", "preco": 30.00},
            "6": {"nome": "Frango com Catupiry", "preco": 35.00},
            "7": {"nome": "Carne Seca", "preco": 35.00}
        }
        self.menu_bebidas = {
            "1": {"nome": "Refrigerante", "preco": 7.00},
            "2": {"nome": "Suco Natural", "preco": 6.50},
            "3": {"nome": "Refrigerante 2L", "preco": 15.00}
        }
        self.menu_refrigerantes = {
            "1": {"nome": "Sprite", "preco": 7.00},
            "2": {"nome": "Coca-Cola", "preco": 7.00},
            "3": {"nome": "Fanta Laranja", "preco": 7.00},
            "4": {"nome": "Fanta Uva", "preco": 7.00},
            "5": {"nome": "Pepsi", "preco": 7.00}
        }
        self.menu_sucos = {
            "1": {"nome": "Suco de Goiaba", "preco": 6.50},
            "2": {"nome": "Suco de Laranja", "preco": 6.50},
            "3": {"nome": "Suco de Uva", "preco": 6.50},
            "4": {"nome": "Suco de Morango", "preco": 6.50}
        }
        self.menu_refrigerantes_2l = {
            "1": {"nome": "Coca-Cola 2L", "preco": 15.00},
            "2": {"nome": "Fanta Uva 2L", "preco": 15.00},
            "3": {"nome": "Fanta Laranja 2L", "preco": 15.00},
            "4": {"nome": "Pepsi 2L", "preco": 15.00}
        }
        self.pedido = []

    def mostrar_menu(self, tipo):
        print(f"{MAGENTA}{'=' * 30} Menu de {tipo.capitalize()}s {'=' * 30}{RESET}")
        menu = self.menu_pizzas if tipo == 'pizza' else self.menu_bebidas
        print(f"{MAGENTA}{'Código'.center(20)}{'Produto'.center(40)}{'Preço'.center(20)}{RESET}")
        for key, item in menu.items():
            print(f"{BRANCO_NEGRITO}{key.center(20)}{item['nome'].center(40)}{'R$ {:.2f}'.format(item['preco']).center(20)}{RESET}")
        print(f"{MAGENTA}{'=' * 78}{RESET}")

    def mostrar_menu_refrigerantes(self):
        print(f"\n{MAGENTA}{'=' * 30} Menu de Refrigerantes {'=' * 30}{RESET}")
        print(f"{MAGENTA}{'Código'.center(20)}{'Produto'.center(40)}{'Preço'.center(20)}{RESET}")
        for key, refri in self.menu_refrigerantes.items():
            print(f"{BRANCO_NEGRITO}{key.center(20)}{refri['nome'].center(40)}{'R$ {:.2f}'.format(refri['preco']).center(20)}{RESET}")
        print(f"{MAGENTA}{'=' * 78}{RESET}")

    def mostrar_menu_sucos(self):
        print(f"\n{MAGENTA}{'=' * 30} Menu de Sucos Naturais {'=' * 25}{RESET}")
        print(f"{MAGENTA}{'Código'.center(20)}{'Produto'.center(40)}{'Preço'.center(20)}{RESET}")
        for key, suco in self.menu_sucos.items():
            print(f"{BRANCO_NEGRITO}{key.center(20)}{suco['nome'].center(40)}{'R$ {:.2f}'.format(suco['preco']).center(20)}{RESET}")
        print(f"{MAGENTA}{'=' * 78}{RESET}")

    def mostrar_menu_refrigerantes_2l(self):
        print(f"\n{MAGENTA}{'=' * 30} Menu de Refrigerantes 2L {'=' * 22}{RESET}")
        print(f"{MAGENTA}{'Código'.center(20)}{'Produto'.center(40)}{'Preço'.center(20)}{RESET}")
        for key, refri in self.menu_refrigerantes_2l.items():
            print(f"{BRANCO_NEGRITO}{key.center(20)}{refri['nome'].center(40)}{'R$ {:.2f}'.format(refri['preco']).center(20)}{RESET}")
        print(f"{MAGENTA}{'=' * 78}{RESET}")

    def escolher_item(self, menu):
        while True:
            escolha = input(f"\n{BRANCO_NEGRITO}Digite o código do item desejado (ou 'sair' para voltar): {RESET}").strip()
            print("\n")
            if escolha in menu:
                self.pedido.append(menu[escolha])
                print(f"{AMARELO}Processando...{RESET}")
                time.sleep(2)
                print(f"{VERDE}Adicionado: {menu[escolha]['nome']}{RESET}\n")
                time.sleep(2)
                break
            elif escolha.lower() == 'sair':
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def escolher_bebida(self):
        while True:
            bebida = input(f"\n{MAGENTA}Escolha a opção desejada: {RESET}").strip()
            if bebida == '1':
                self.mostrar_menu_refrigerantes()
                self.escolher_item(self.menu_refrigerantes)
                break
            elif bebida == '2':
                self.mostrar_menu_sucos()
                self.escolher_item(self.menu_sucos)
                break
            elif bebida == '3':
                self.mostrar_menu_refrigerantes_2l()
                self.escolher_item(self.menu_refrigerantes_2l)
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def adicionar_pedido(self):
        while True:
            escolha_menu = input(f"{BRANCO_NEGRITO}1. Ver menu de Pizzas.\n2. Ver menu de Bebidas.\n3. Prosseguir para o pagamento.\n4. Encerrar o Atendimento.\n\n{RESET}{MAGENTA}Digite a opção desejada: {RESET}").strip()
            if escolha_menu == '1':
                print(f"\n{AMARELO}Irei exibir o menu de pizzas para você!")
                time.sleep(1)
                print(f"{AMARELO}Um segundo...\n")
                time.sleep(2)
                self.mostrar_menu('pizza')
                self.escolher_item(self.menu_pizzas)
            elif escolha_menu == '2':
                print(f"\n{AMARELO}Irei exibir o menu de bebidas para você!")
                time.sleep(1)
                print(f"{AMARELO}Um segundo...")
                time.sleep(2)
                self.mostrar_menu('bebida')
                self.escolher_bebida()
            elif escolha_menu == '3':
                break
            elif escolha_menu == '4':
                print(f"\n{CINZA}Encerrando o atendimento...{RESET}")
                time.sleep(2)
                print(f"{VERDE}Atendimento encerrado. Até logo!{RESET}")
                exit()
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def mostrar_resumo_pedido(self):
        print(f"\n{MAGENTA}{'=' * 30} Resumo do Pedido {'=' * 30}{RESET}")
        total = 0
        for item in self.pedido:
            print(f"{BRANCO_NEGRITO}{item['nome']} - R$ {item['preco']:.2f}{RESET}".center(80))
            total += item['preco']
        print(f"{AZUL}TOTAL: R$ {total:.2f}{RESET}".center(80))
        print(f'{MAGENTA}={RESET}' * 78)
        return total

    def confirmar_pedido(self):
        while True:
            total = self.mostrar_resumo_pedido()
            confirmacao = input(f"\n{MAGENTA}(S) Sim.\n(N) Não.\n\nDeseja confirmar o seu pedido?  {RESET}").strip().lower()
            if confirmacao == 's':
                self.opcoes_pagamento()
                break
            elif confirmacao == 'n':
                self.modificar_pedido()
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def modificar_pedido(self):
        while True:
            acao = input(f"{BRANCO}\nR = Retirar.\nA = Adicionar.\n\n{RESET}{MAGENTA}Digite a opção desejada: {RESET}").strip().lower()
            if acao == 'r':
                self.retirar_item()
                self.confirmar_pedido()  
                break
            elif acao == 'a':
                self.adicionar_pedido()
                self.confirmar_pedido() 
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def retirar_item(self):
        if not self.pedido:
            print(f"{VERMELHO}Nenhum item para retirar.{RESET}")
            return
        print(f"\n{MAGENTA}{'=' * 30} Pedidos Efetuados {'=' * 30}{RESET}")
        for idx, item in enumerate(self.pedido, 1):
            print(f"{idx}. {item['nome']} - R$ {item['preco']:.2f}".center(80))
            print(f"{MAGENTA}{'=' * 78}{RESET}")
        while True:
            escolha = input(f"\n{BRANCO}Escolha o código do item para retirar: {RESET}").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(self.pedido):
                item_removido = self.pedido.pop(int(escolha) - 1)
                print(f"\n{AMARELO}Processando...{RESET}")
                time.sleep(2)
                print(f"{VERMELHO}Removido: {item_removido['nome']}{RESET}")
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def opcoes_pagamento(self):
        total = self.mostrar_resumo_pedido()
        print(f"\n{AZUL}{'=' * 28} Opções de Pagamento {'=' * 29}{RESET}".center(80))
        while True:
            pagamento = input((f"{BRANCO_NEGRITO}\n1. Débito\n2. Crédito\n3. Dinheiro\n\n{RESET}{AZUL}{'=' * 78}\n\nEscolha a opção de pagamento desejada: {RESET}").center(80)).strip()
            if pagamento == '1':
                print(f"\n{AMARELO}Pagamento via Débito sendo processado...{RESET}")
                time.sleep(2)
                print(f"{VERDE}Pagamento Efetuado!{RESET}")
                time.sleep(1)
                print(f"{MAGENTA}Obrigado pela preferência, seu pedido deve chegar em breve! Até Logo!")
                print('\n')
                break
            elif pagamento == '2':
                print(f"\n{AMARELO}Pagamento via Crédito sendo processado...{RESET}")
                time.sleep(2)
                print(f"{VERDE}Pagamento Efetuado!{RESET}")
                time.sleep(1)
                print(f"{MAGENTA}Obrigado pela preferência, seu pedido deve chegar em breve! Até Logo!")
                print('\n')
                break
            elif pagamento == '3':
                self.pagamento_dinheiro(total)
                break
            else:
                print(f"{VERMELHO}Escolha inválida. Tente novamente.{RESET}")

    def pagamento_dinheiro(self, total):
        while True:
            try:
                dinheiro = float(input(f"{BRANCO}Digite o valor do dinheiro entregue: R$ {RESET}"))
                if dinheiro >= total:
                    troco = dinheiro - total
                    print(f"\n{MAGENTA}Pagamento via Dinheiro sendo processado...{RESET}")
                    time.sleep(2)
                    print(f"{VERDE}Pagamento aceito! Troco: R$ {troco:.2f}{RESET}")
                    time.sleep(2)
                    print(f"{AMARELO}Obrigado pela preferência, seu pedido deve chegar em breve! Até Logo!")
                    print('\n')
                    break
                else:
                    print(f"{VERMELHO}Valor insuficiente! Tente novamente.{RESET}")
            except ValueError:
                print(f"{VERMELHO}Valor inválido! Digite um valor numérico.{RESET}")

def main():
    pizzaria = Pizzaria()
    pizzaria.adicionar_pedido()
    if pizzaria.pedido:
        pizzaria.confirmar_pedido()
    else:
        print(f"{VERMELHO}Pedido vazio. Atendimento encerrado.{RESET}")

if __name__ == "__main__":
    main()