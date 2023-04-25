class veiculo:
    def __int__(self):
        print('entrou na função init...')
        self.id = None #Identificação única no estoque
        self.tipo = None #Carro, moto etc...
        self.marca = None #Chevrolet, etc...
        self.cor = None #Vermelho...
        self.chassi = None # adad342344...
        self.modelo = None #Monza, celta etc...
        self.placa = None #JHC-0043...
        self.n_rodas = None #2, 4 etc...
        self.ano = None # 2012
        self.preco = None # 12.555
    def cadastro(self):
        self.tipo = int(input('Digite o tipo do veiculo: 1) Carro 2) Moto: '))
        #self.cor = str(input('Digite a cor do veiculo (ex: vermelho): '))
        self.ano = int(input('Digite o ano do veiculo (ex: 2023): '))
        #self.preco = float(input('Digite o valor do veículo (ex: 8539.99): '))
    def mostrar(self, id):
        print(f'Id: {id}')
        print(f'Tipo do veiculo: {self.tipo}')
        #print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        #print(f'Valor R${self.preco}')

estoque = [] # armazena veiculo

while True:
    print('Oque você dejesa fazer? 1) Cadastrar veiculo, 2) mostrar estoque, 0) sair')
    opcao = int(input('Digite uma opção desejada: '))

    if opcao == 1:
        Veiculo = veiculo()
        Veiculo.cadastro()
        estoque.append(Veiculo)
    elif opcao == 2:
        print('------- Veiculos Disponiveis ------')
        for id, veiculo in enumerate(estoque):
            veiculo.mostrar(id)

    elif opcao == 0:
        print('Obrigado pela preferência!')
        break