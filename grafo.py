#Operações básicas:
#1- Criar o grafo
#2 – Adicionar Nós e Arcos Rotulados. Ou seja, o sistema deve pedir o nome do nó e o peso do arco.
#3 – Pesquisar um nó ou arco no grafo pelo nome, origem e/ou destino
    
class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
    def igualA(self, r):
        return r == self.rotulo

class Grafo:
    def __init__(self):
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.listaVertices = []
        self.listaArcos = []
        self.matrizAdjacencias = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz = []
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)

    def adicionaVertices(self, rotulo):
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))

    def adicionaArco(self, rotulo, peso, inicio, fim, rotuloInicio, rotuloFim):
        self.listaArcos.append([rotulo, rotuloInicio, rotuloFim])
        self.matrizAdjacencias[inicio][fim] = peso
        self.matrizAdjacencias[fim][inicio] = peso

    def imprimeMatriz(self):
        print(" ", end=" ")
        for i in range(0, self.numVertices):
            print(self.listaVertices[i].rotulo, end=" ")
        print(" ")
        for i in range(0, self.numVertices):
            print(self.listaVertices[i].rotulo, end=" ")
            for j in range(0, self.numVertices):
                print(self.matrizAdjacencias[i][j], end=" ")
            print(" ")

    def localizaNo(self, rotulo):
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo):
                return i
        return -1

    def localizaArco(self, rotulo):
        for i in range(len(self.listaArcos)):
            if self.listaArcos[i][0] == rotulo:
                return i
        return -1

    def localizaPorOrigemDestino(self, rotulo):
        lista_retorno = []
        for i in range(0, len(self.listaArcos)):
            if self.listaArcos[i][1] == rotulo or self.listaArcos[i][2] == rotulo:
                lista_retorno.append(self.listaArcos[i][0])
        if len(lista_retorno) == 0:
            return -1
        return lista_retorno


if __name__ == "__main__":
    grf = Grafo()
    while True:
        print("\n")
        print("********** Escolha uma opção: **********\n")
        print("1 - Mostrar\n")
        print("2 - Inserir vértice\n")
        print("3 - Inserir Arco \n")
        print("4 - Buscar \n")
        print("5 - Sair\n")
        escolha = input("Escolha uma opção:")
        print("*****************************************")
        if escolha == "1":
            grf.imprimeMatriz()
        elif escolha == "2" :
            val = input("Digite o rótulo do vertice a inserir: ")
            grf.adicionaVertices(val)
        elif escolha == "3":
            rotulo = input("Digite o rótulo do arco: ")
            peso = int(input("Digite o peso do arco: "))
            rinicio = input("Digite o rótulo do vértice de início do arco: ")
            inicio = grf.localizaNo(rinicio)
            if inicio == -1:
                print("Vértice não encontrado. Cadastre o vértice primeiro.")
                input()
                continue
            rfim = input("Digite o rótulo do vértice de fim do arco: ")
            fim = grf.localizaNo(rfim)
            if fim == -1:
                print("Vértice não cadastrado. Cadastre o vértice primeiro")
                input()
                continue
            grf.adicionaArco(rotulo, peso, inicio, fim, rinicio, rfim)
        elif escolha == "5":
            break
        elif escolha == "4":
            escolha2 = input("Buscar nó ou arco? \n(2) - Nó      (3) - Arco")
            if escolha2 == "2":
                escolha2 = input("Digite o rótulo do nó: ")
                if grf.localizaNo(escolha2) == -1:
                    print("Nó não encontrado!")
                else:
                    print("Nó encontrado!")
            elif escolha2 == "3":
                escolha2 = input("Buscar por nome ou origem/destino? \n(N) - Nome         (O) - Origem/Destino")
                if escolha2 == "N" or escolha2 == "n":
                    nome = input("Digite o rótulo do arco a ser pesquisado:")
                    if grf.localizaArco(nome) == -1:
                        print("Arco não encontrado!")
                    else:
                        print("Arco encontrado!")
                elif escolha2 == "O" or escolha2 == "o":
                    escolha2 = input("Digite o nome do vértice de origem ou destino: ")
                    resposta = grf.localizaPorOrigemDestino(escolha2)
                    if resposta == -1:
                        print("O arco selecionado não foi encontrado!")
                    else:
                        print("O arco selecionado foi encontrado! Seu nome é ", end=" ")
                        print(resposta)

        else:
            input("Entrada inválida. Pressione Enter")