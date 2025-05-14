class Restaurante:

    def __init__(self):
        self.cardapio = {}
        self.comanda = {}

### 1 - Adicionar o cardápio
    def adicionar_prato(self):
        nome = input("Digite o nome do prato: ")
        while True:
            try:
                preco = float(input("Digite o preço do prato: "))
                break
            except:
                print("Preço inválido")
        
        while True:
            try:
                tempo = int(input("Digite o tempo de preparo (em minutos): "))
                break
            except:
                print("Tempo inválido. Digite um número inteiro.")

        self.cardapio[nome] = preco
        self.cardapio[nome] = {"preco": preco, "tempo_preparo": tempo}
        print(f"O prato {nome} foi adicionado")

### 2 - Abrir comanda
    def abrir_comanda(self):
        while True:
            numero = int(input("Digite o número da comanda: "))
            if numero in self.comanda:
                print(f"Comanda de número {numero} já está aberta")
                decisao = input("Deseja cancelar? S/N ").lower()
                if decisao == "s":
                    return
            else:
                self.comanda[numero] = {"pratos": [], "total":0, "status": "Aberta", "forma_pagamento": "-"}
                print(f"A comanda {numero} foi aberta com sucesso!")
                return

### 3 - Adicionar pedido
    def adicionar_pedido(self):
        numero = int(input("Digite o número da comanda: "))
        if numero not in self.comanda:
            print(f"Comanda número {numero} não encontrada")
            return

        print("-" * 30)
        print(f"Cardápio disponível:")
        for nome, dados in self.cardapio.items():
            print(f"Prato: {nome} Preço: {dados['preco']:.2f} Tempo de preparo: {dados['tempo_preparo']} min")
        
        print("-" * 30)
        while True:
            prato = input("Digite o nome do prato para adicionar ao pedido: ")
            if prato in self.cardapio:
                self.comanda[numero]["pratos"].append(prato)
                self.comanda[numero]['total'] += self.cardapio[prato]['preco']
                self.comanda[numero]['status'] = "Em preparo"
                print(f"{prato} adicionado com sucesso!")
                decisao = input("Deseja anotar mais algum pedido? S/N ").lower()
                if decisao == "n":
                    return
            else:
                print(f"O prato {prato} não existe no cardápio")
                decisao = input("Deseja anotar mais algum pedido? S/N ").lower()
                if decisao == "n":
                    return

### 4 - Verificar pedido
    def verificar_pedido(self):
        while True:
            try:
                numero = int(input("Digite o número da comanda: "))
                if numero not in self.comanda:
                    print("Comanda não encontrada")
                    return
                print("-" * 30)
                print(f"\n Comanda {numero} ")
                print(f"\n Status: {self.comanda[numero]['status']}")
                print(f"Total: {self.comanda[numero]['total']:.2f}")
                print("-" * 30)
                return
                
            except:
                print("Número inválido")
        
### 5 - Fechar a conta
    def fechar_conta(self):
        while True:
            try:
                numero = int(input("Digite o número da comanda: "))
                if numero not in self.comanda:
                    print("Comanda não encontrada")
                    return
                
                if self.comanda[numero]['status'] == "Aberta" or self.comanda[numero]['status'] == "Em preparo":
                    print("O pedido está sendo preparado")
                    decisao = input("Deseja encerrar a conta? S/N ").lower()
                    if decisao == 's':
                        self.comanda[numero]['status'] = "Fechada"
                        print(f"\n Conta da Comanda {numero} fechada")
                        print(f"Total a pagar: R${self.comanda[numero]['total']}")
                        pagamentos_permitidos = ['credito', "debito", "dinheiro", "pix"]
                        while True:
                            pagamento = input("Digite a forma de pagamento: (credito, debito, pix ou dinheiro) ")
                            if pagamento in pagamentos_permitidos:
                                self.comanda[numero]['forma_pagamento'] = pagamento
                                print("Pagamento efetuado com sucesso!")
                                break
                            else:
                                print("Forma de pagamento inválida, tente novamente")

                        del self.comanda[numero]
                        return
                    return
                
                print(f"\n Conta da Comanda {numero} já está fechada")
                return
            
            except:
                print("Número inválido")

seven = Restaurante()

while True:
    print("------------Opções disponíveis------------")
    print("1 - Adicionar ao cardápio")
    print("2 - Abrir comanda")
    print("3 - Adicionar pedido")
    print("4 - Verificar pedido")
    print("5 - Fechar a conta")
    print("6 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        seven.adicionar_prato()
    elif opcao == "2":
        seven.abrir_comanda()
    elif opcao == "3":
        seven.adicionar_pedido()
    elif opcao == "4":
        seven.verificar_pedido()
    elif opcao == "5":
        seven.fechar_conta()
    elif opcao == "6":
        print("Encerrando sistema")
        break
    else:
        print("Opção inválida")