#Aula de Tuplas, Dicinarios e listas
#Ultima School

#listas compostas - ficam entre colchetes
nomes = ['Junior', 'Wyllon', 'Kamila', 'Carlos', 'Sherlon', 'João']
#Len() -> Lenght -> Tamanho/Comprimento
#Indices:

for i in (nomes):
    print(i)

nome = [] # Armazene as informações dos clientes
for i in range(3):
    name = str(input('Digite seu nome: '))
    nome.append(name)
    print(nome, len(nome))

#Tuplas - São imutaveis ficam entre parenteses
nomes = ('Sherlon', 'Daniel', 'Kamila', 'Wyllon', 'Igor')
print(nomes)


#Dicionarios = não utiliza somente indices mas tambem - utiliza Chaves  {Chave: valor}:
cliente = {'Nome': 'Igor', 'Idade': 27, 'Senha': '12345'}

senha_cliente = '12345'
if cliente['Senha'] == senha_cliente:
    print('Acesso liberado!')
else:
    print('Senha invalida!')
    cliente['Senha'] = input('Digite uma nova senha: ')
print(cliente)

cliente = {'Nome': 'Igor', 'Idade': 27, 'Senha': '12345'}
print(cliente.keys())
print(cliente.values())
print(cliente.items())

def exemplo(*args):
    print(num, type(num))
num = (1, 0,2 ,3 )
exemplo(exemplo)

#Classes 
class Cliente:
    def __init__(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None
    
    def cadastro(self):
        self.nome  = input('Digite o nome: ')
        self.cpf   = input('Digite o CPF: ')
        self.idade = int(input('Digite sua idade: '))
    
    def mostrar_dados(self):
        print('Nome: ', self.nome)
        print('CPF: ', self.cpf)
        print('Idade: ', self.idade)

clientes = []
for i in range(2):
    cliente = Cliente()
    cliente.cadastro()
    cliente.mostrar_dados
    clientes.append(cliente)
print(clientes[0])



        