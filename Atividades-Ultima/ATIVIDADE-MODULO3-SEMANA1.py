import requests

#Classe modelo para iteração com API
class Modelos:
    def __init__(self, codigo: str):
        #Variavél para armazenar URL da API
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']
            self.passo = 0
            self.tamanho = len(self.modelos)
        else:
            print('Erro 404! Falha ao carregar!')

    def __iter__(self):
        self.passo = 0
        return self

    def __next__(self):
        if self.passo >= self.tamanho:
            raise StopIteration
        resposta: object = list(self.modelos)[self.passo]
        self.passo = self.passo + 1
        return resposta

resp = str(input('Digite o Código dos modelos: '))
mod = Modelos(resp)
for i in mod:
    print(i)