class Loja:
    def __init__(self):
        # Simulação de catálogo de produtos com preços
        self.produtos = {
            1: {'nome': 'Produto A', 'preco': 100},
            2: {'nome': 'Produto B', 'preco': 200},
            3: {'nome': 'Produto C', 'preco': 150},
            4: {'nome': 'Produto D', 'preco': 250},
        }
        # Carrinho de compras do cliente
        self.carrinho = []
        # Desconto padrão
        self.desconto = 0

    def exibir_produtos(self):
        print("\nProdutos disponíveis na loja:")
        for id_produto, produto in self.produtos.items():
            print(f"{id_produto}. {produto['nome']} - R${produto['preco']}")

    def adicionar_ao_carrinho(self, id_produto):
        if id_produto in self.produtos:
            produto = self.produtos[id_produto]
            self.carrinho.append(produto)
            print(f"{produto['nome']} foi adicionado ao seu carrinho.")
        else:
            print("Produto inválido! Tente novamente.")

    def aplicar_desconto(self):
        if len(self.carrinho) >= 3:  # Se o cliente comprar 3 ou mais produtos, aplica 10% de desconto
            self.desconto = 0.10
            print("Você ganhou 10% de desconto pela compra de 3 ou mais produtos!")
        else:
            print("Nenhum desconto aplicado.")

    def exibir_resumo_compra(self):
        if not self.carrinho:
            print("Seu carrinho está vazio. Adicione produtos antes de finalizar a compra.")
            return

        total = sum(produto['preco'] for produto in self.carrinho)
        desconto = total * self.desconto
        total_com_desconto = total - desconto

        print("\nResumo da sua compra:")
        for produto in self.carrinho:
            print(f"- {produto['nome']} - R${produto['preco']}")
        
        print(f"\nTotal: R${total}")
        if self.desconto > 0:
            print(f"Desconto aplicado: R${desconto}")
        print(f"Total com desconto: R${total_com_desconto}")

    def finalizar_compra(self):
        self.exibir_resumo_compra()
        if self.carrinho:
            print("\nCompra finalizada com sucesso!")
            self.carrinho = []  # Limpa o carrinho após a compra
            self.desconto = 0  # Reseta o desconto

def main():
    loja = Loja()

    while True:
        print("\nBem-vindo à loja! O que você gostaria de fazer?")
        print("1. Ver produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver resumo da compra")
        print("4. Finalizar compra")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.exibir_produtos()
        elif opcao == "2":
            loja.exibir_produtos()
            try:
                id_produto = int(input("Digite o número do produto que deseja adicionar ao carrinho: "))
                loja.adicionar_ao_carrinho(id_produto)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "3":
            loja.exibir_resumo_compra()
        elif opcao == "4":
            loja.aplicar_desconto()
            loja.finalizar_compra()
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
