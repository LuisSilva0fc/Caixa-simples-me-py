# Caixa de Registradora de Vendas e Produtos
# Obs: Para não sobrecarregar de comentários, ja que um programa que possui diversas "sintaxe repetitivas" iremos fazer comentários das principais funções base...

# "Listas para armazenar o Dicionário" dos produtos e registro de cliente
produtos = []
histórico_de_vendas = []

# Função de adicionar produto ao caixa
def adicionar_produto(): # Criando e nomeado função por meio do "def"...
    print('\n')
    print('▬' * 30)
    print('──｢Adicionar Produto ao Caixa｣──')
    nome = input('Digite o nome do produto: ') # Solicita ao usuário que insira o nome do produto...
    
    while True: # Iniciar um "loop"...
        preco = input('Digite o preço do produto: ')# Solicita ao usuário que insira o preço do produto...
        try: # Tenta converter o preço para um número de ponto flutuante...
            preco = float(preco.replace(',', '.')) # Substitui a vírgula por ponto e converte para float graças o ".replace"...
            break # Sai do loop se a conversão for bem-sucedida...
        except ValueError: # Captura a exceção se a conversão falhar...
            print('Caractere proibido! Por favor, digite um número válido. Use "." para separar decimais.')
    
    while True:
        quantidade = input('Digite a quantidade do produto: ')
        try:
            quantidade = int(quantidade)# Converte a quantidade para inteiro...
            break
        except ValueError:
            print('\nCaixa > Caractere proibido! Por favor, digite um número inteiro válido.\n')
    
    produto = {'Nome': nome, 'Preço': preco, 'Quantidade': quantidade} # Cria um dicionário com as informações do produto, com seguinte formatação {"Palavra Chave": Variável)...
    produtos.append(produto) # Adiciona o dicionário à lista de produtos...
    print('\nCaixa > Produto adicionado com sucesso!\n')
    print('▬' * 30)

# Função para listar produtos do caixa
def listar_produtos():
    print('\n')
    print('▬' * 30)
    print('──｢Listar Produtos｣──')
    if produtos: # Verifica se a lista de produtos não está vazia...
        for produto in produtos: # Itera sobre cada produto na lista de produtos...
            nome = produto["Nome"] # Obtém "variável=nome" do "Dicionario=produto"...
            preco = produto["Preço"]
            quantidade = produto["Quantidade"]
            print(f'Nome: {nome} - Preço: R${preco:.2f} - Quantidade: {quantidade}') # Exibe as informações do produto formatadas; ".2f" para pegar os 2 primeiros números após do "." ao invés do "round", para arrendondar o número...
    else:
        print('\nCaixa > Nenhum produto cadastrado...\n') # Exibe uma mensagem se não houver produtos cadastrados, graças ao "else"...
        print('▬' * 30)

# Função de buscar produtos do caixa (Tentativa 46 ~_~)
def buscar_produto():
    print('\n')
    print('▬' * 30)
    print('──｢Buscar Produto｣──')
    criterio = input('Digite "n" para buscar por nome ou "v" para buscar por valor: ').strip().lower() # .strip(): Remove todos os espaços em branco do início e do final da string; .lower(): Converte todos os caracteres da string para minúsculas.
    
    if criterio == 'n': # Verifica se o critério é buscar por nome...
        nome = input('Digite o nome ou a letra inicial do produto a ser buscado: ').strip().lower() # Solicita o nome ou a inicial do produto e normaliza a entrada; ".strip" para remoção de espaços brancos e ".lower" para converter a "string"...
        produtos_encontrados = [produto for produto in produtos if produto['Nome'].lower().startswith(nome)] # Busca produtos cujo nome começa com a string fornecida...
    elif criterio == 'v': # Verifica se o critério é buscar por valor...
        while True:
            valor = input('Digite o valor do produto a ser buscado: ').strip() # Solicita o valor do produto e remove os espaços brancos com ".strip"...
            try:
                valor = float(valor.replace(',', '.'))
                break
            except ValueError:
                print('\nCaixa > Caractere proibido! Por favor, digite um número válido.\n')
        produtos_encontrados = [produto for produto in produtos if produto['Preço'] == valor] # Cria uma lista de produtos cujo preço é igual ao valor fornecido...
    else:
        print('\nCaixa > Critério inválido. Por favor, digite "n" para nome ou "v" para valor.\n')
        return # Evita a execução de qualquer código após a atualização bem-sucedida do produto e volta ao ponto "inicial".
    
    if produtos_encontrados:
        for produto in produtos_encontrados:
            print(f'➤ Produto encontrado: \n Nome: {produto["Nome"]} - Preço: R${produto["Preço"]:.2f} - Quantidade: {produto["Quantidade"]}')
    else:
        print('\nCaixa > Produto não encontrado...\n')
        print('▬' * 30)

# Função para editar produtos do caixa
def editar_produto():
    print('\n')
    print('▬' * 30)
    print('──｢Editar Produto｣──')
    nome = input('Digite o nome do produto a ser editado: ')
    for produto in produtos: # Verifica se existe algum nome que corresponde um produto do dicionario...
        if nome == produto['Nome']: # Verifica se o nome é exatamente igual
            print(f'➤ Produto encontrado: \n Nome: {produto["Nome"]} - Preço: R${produto["Preço"]:.2f} - Quantidade: {produto["Quantidade"]}')
            
            while True:
                novo_preco = input('Digite o novo preço do produto: ')
                try:
                    novo_preco = float(novo_preco.replace(',', '.'))
                    break
                except ValueError:
                    print('\nCaixa > Caractere proibido! Por favor, digite um número válido. Use "." ou "," para separar as decimais.\n')
            
            while True:
                nova_quantidade = input('Digite a nova quantidade do produto: ')
                try:
                    nova_quantidade = int(nova_quantidade)
                    break
                except ValueError:
                    print('\nCaixa > Caractere proibido! Por favor, digite um número inteiro válido.\n')
            
            produto['Preço'] = novo_preco # Atualiza o produto
            produto['Quantidade'] = nova_quantidade
            print(f'➤ Produto {produto["Nome"]} atualizado com sucesso!')
            print('▬' * 30)
            return
    print('\nCaixa > Produto não encontrado...\n')
    print('▬' * 30)

# Função para remover produto do caixa
def remover_produto():
    print('\n')
    print('▬' * 30)
    print('\n──｢Remover Produto｣──')
    nome = input('Digite o nome do produto a ser removido: ')
    for produto in produtos:
        if nome == produto['Nome']: 
            print(f'➤ Produto encontrado: \nNome: {produto["Nome"]} - Preço: R${produto["Preço"]:.2f} - Quantidade: {produto["Quantidade"]}')
            produtos.remove(produto) # Uso da função ".remuve(variável)", para remover item da lista/dicionario...
            print('Produto removido com sucesso!')
            return
    print('\nCaixa > Produto não encontrado...\n')
    print('▬' * 30)

# Função para registrar venda do caixa
def registrar_venda():
    print('\n')
    print('▬' * 30)
    print('──｢Registrar Venda｣──')
    cliente = input('Digite o nome do cliente: ')
    total = 0  # Inicializa a variável total para armazenar o valor total da venda
    
    while True:
        nome_produto = input('\nDigite o nome do produto (ou "f" para finalizar): ')
        print('\n')
        if nome_produto == 'f':
            break
        tipo_pg = input('Tipo de pagamento:\n1 - Cartão\n2 - Dinheiro\n3 - Fiado\nDigite a opção: ')

        produto_encontrado = False
        for produto in produtos:
            if nome_produto == produto['Nome']:
                produto_encontrado = True
                quantidade = int(input('Digite a quantidade: '))
                if quantidade <= produto['Quantidade']:  # Verifica se há quantidade suficiente em estoque
                    produto['Quantidade'] -= quantidade  # Reduz a quantidade em estoque
                    total += produto['Preço'] * quantidade  # Adiciona o valor do produto ao total da venda
                    histórico_de_vendas.append({'Cliente': cliente, 'Produto': nome_produto, 'Quantidade': quantidade, 'Preço': produto['Preço'], 'Tipo de Pagamento': tipo_pg})  # Adiciona a venda à lista de vendas do cliente
                else:
                    print('\nCaixa > Quantidade insuficiente em estoque.\n')
                break

        if not produto_encontrado:
            print('\nCaixa > Produto não encontrado.\n')
        print('▬' * 30)
    
    print(f'Valor total da venda: R${total:.2f}\n')
    print('▬' * 30)

# Função para listar clientes, suas compras e tipo de pagamento
def listar_cliente():
    print('\n')
    print('▬' * 30)
    print('──｢Listar Clientes e Pendências｣──')
    if histórico_de_vendas:  # Verifica se a lista de clientes não está vazia
        for cliente in histórico_de_vendas:  # Itera sobre cada cliente na lista de clientes
            print(f'Cliente: {cliente["Cliente"]}')  # Exibe o nome do cliente
            for compra in cliente["Compras"]:  # Itera sobre cada compra do cliente
                produto = compra["Produto"]
                quantidade = compra["Quantidade"]
                preco = compra["Preço"]
                tipo_pg = compra["Tipo de Pagamento"]
                print(f'  Produto: {produto} - Quantidade: {quantidade} - Preço: R${preco:.2f} - Tipo de Pagamento: {tipo_pg}')  # Exibe as informações da compra formatadas
            print(f'Total: R${cliente["Total"]:.2f}')  # Exibe o total das compras do cliente
            if any(compra['Tipo de Pagamento'] == 'Fiado' for compra in cliente['Compras']):  # Verifica se alguma compra foi fiada
                print('  Cliente está devendo.')
            print('▬' * 30)
    else:
        print('\nCaixa > Nenhum cliente encontrado...\n')  # Exibe uma mensagem se não houver clientes cadastrados
        print('▬' * 30)

# Função de buscar cliente do caixa (Obs: para a buscar é necessário digitar nome exato...)
def buscar_cliente():
    print('\n')
    print('▬' * 30)
    print('──｢Buscar Cliente｣──')
    nome = input('Digite o nome do cliente a ser buscado: ')
    print('\n')
    for cliente in histórico_de_vendas:
        if nome == cliente['Cliente']:
            print(f'➤ Cliente encontrado: \n Nome: {cliente["Cliente"]}')
            for compra in cliente['Compras']:
                print(f'  Produto: {compra["Produto"]} - Quantidade: {compra["Quantidade"]} - Preço: R${compra["Preço"]:.2f} - Tipo de Pagamento: {compra["Tipo de Pagamento"]}')
            print(f'Total: R${cliente["Total"]:.2f}')
            if cliente['Tipo de Pagamento'] == '3':
                print('  Cliente está devendo.\n')
                print('▬' * 30)
                print('\n')
            return
    print('\nCaixa > Cliente não encontrado...\n')
    print('▬' * 30)

#Função para remover pendencias do meio de pagamento fiado
def remover_pendencia():
    print('\n')
    print('▬' * 30)
    print('──｢Remover Pendência de Cliente｣──')
    nome_cliente = input('Digite o nome do cliente: ')

    for vendas_cliente in histórico_de_vendas:
        if nome_cliente == vendas_cliente['Nome']:  # Verifica se o nome do cliente corresponde ao nome fornecido
            if vendas_cliente['Tipo de Pagamento'] == '3':  # Verifica se o tipo de pagamento foi fiado
                vendas_cliente['Tipo de Pagamento'] = 'Pago'  # Atualiza o status de pagamento para "Pago"
                print(f'\n➤ Pendência do cliente {vendas_cliente["Nome"]}, removida com sucesso!\n')
                print('▬' * 30)
                print('\n')
                return
            else:
                print('\nCliente não possui pendências fiadas.\n')
                print('▬' * 30)
                print('\n')
                return
    print('Cliente não encontrado.')
    print('▬' * 30)
    print('\n')

# Créditos do mini projeto
def sobre_nos():
    print('┌──────⎾Envolvidos no projeto⏌────────────')
    print('├ Luis Fernando Bento da Silva\n├ Kauennio Iarley Dantas Vieira\n├ Israel Oliveira do Nascimento\n├ Maria Eduarda Soares Domingos Dos Santos\n├ Mykaelle Ramos da Silva\n├ Stefny Karla Barbosa Silva\n└─────────────────────────────────────────')

# Função de menu para categoria cliente
def menu_clientes():
    while True:
        print('\n')
        print('▬' * 30)
        print('──｢Menu de Clientes｣──\n➤ 1 - Listar Clientes e Histórico de Pagamento;\n➤ 2 - Procurar Cliente e Histórico de Pagamento;\n➤ S - Sair;')
        print('▬' * 30)
        opcao = input('Digite a opção desejada: ')
        print('▬' * 30)
        if opcao.lower() == 's':
            break
        elif opcao == '1':
            listar_cliente()
        elif opcao == '2':
            buscar_cliente()
        else:
            print('\nCaixa > Opção inválida, tente novamente.\n')

# Função de menu para categoria produtos
def menu_produtos():
    while True:
        print('▬' * 30)
        print('──｢Menu de Produtos｣──\n➤ 1 - Adicionar Produto;\n➤ 2 - Listar Produtos;\n➤ 3 - Buscar Produto;\n➤ 4 - Editar Produto;\n➤ 5 - Remover Produto;\n➤ 6 - Registrar Venda;\n➤ S - Sair;')
        print('▬' * 30)
        opcao = input('Digite a opção desejada: ')
        print('▬' * 30)
        if opcao.lower() == 's':
            break
        elif opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            buscar_produto()
        elif opcao == '4':
            editar_produto()
        elif opcao == '5':
            remover_produto()
        elif opcao == '6':
            registrar_venda()
        else:
            print('\nCaixa > Erro... Opção inválida, tente novamente.\n')

# Painel do Caixa
def main():
    while True:
        print('▬' * 30)
        print('──｢Menu Principal｣──\n➤ 1 - Menu de Produtos;\n➤ 2 - Menu de Clientes;\n➤ 3 - Sobre nós;\n➤ S - Sair;')
        print('▬' * 30)
        opcao = input('Digite a opção desejada: ')
        print('▬' * 30)
        print('\n')
        if opcao.lower() == 's':
            print('Programa Encerrado...')
            break
        elif opcao == '1':
            menu_produtos()
        elif opcao == '2':
            menu_clientes()
        elif opcao == '3':
            sobre_nos()
        else:
            print('Caixa > Opção inválida, tente novamente.')

if __name__ == "__main__":
    main()