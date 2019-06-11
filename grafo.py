#Opera��es b�sicas:
#1- Criar o grafo
#2 � Adicionar N�s e Arcos Rotulados. Ou seja, o sistema deve pedir o nome do n� e o peso do arco.
#3 � Pesquisar um n� ou arco no grafo pelo nome, origem e/ou destino
    
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
        print("********** Escolha uma op��o: **********\n")
        print("1 - Mostrar\n")
        print("2 - Inserir v�rtice\n")
        print("3 - Inserir Arco \n")
        print("4 - Buscar \n")
        print("5 - Sair\n")
        escolha = input("Escolha uma op��o:")
        print("*****************************************")
        if escolha == "1":
            grf.imprimeMatriz()
        elif escolha == "2" :
            val = input("Digite o r�tulo do vertice a inserir: ")
            grf.adicionaVertices(val)
        elif escolha == "3":
            rotulo = input("Digite o r�tulo do arco: ")
            peso = int(input("Digite o peso do arco: "))
            rinicio = input("Digite o r�tulo do v�rtice de in�cio do arco: ")
            inicio = grf.localizaNo(rinicio)
            if inicio == -1:
                print("V�rtice n�o encontrado. Cadastre o v�rtice primeiro.")
                input()
                continue
            rfim = input("Digite o r�tulo do v�rtice de fim do arco: ")
            fim = grf.localizaNo(rfim)
            if fim == -1:
                print("V�rtice n�o cadastrado. Cadastre o v�rtice primeiro")
                input()
                continue
            grf.adicionaArco(rotulo, peso, inicio, fim, rinicio, rfim)
        elif escolha == "5":
            break
        elif escolha == "4":
            escolha2 = input("Buscar n� ou arco? \n(2) - N�      (3) - Arco")
            if escolha2 == "2":
                escolha2 = input("Digite o r�tulo do n�: ")
                if grf.localizaNo(escolha2) == -1:
                    print("N� n�o encontrado!")
                else:
                    print("N� encontrado!")
            elif escolha2 == "3":
                escolha2 = input("Buscar por nome ou origem/destino? \n(N) - Nome         (O) - Origem/Destino")
                if escolha2 == "N" or escolha2 == "n":
                    nome = input("Digite o r�tulo do arco a ser pesquisado:")
                    if grf.localizaArco(nome) == -1:
                        print("Arco n�o encontrado!")
                    else:
                        print("Arco encontrado!")
                elif escolha2 == "O" or escolha2 == "o":
                    escolha2 = input("Digite o nome do v�rtice de origem ou destino: ")
                    resposta = grf.localizaPorOrigemDestino(escolha2)
                    if resposta == -1:
                        print("O arco selecionado n�o foi encontrado!")
                    else:
                        print("O arco selecionado foi encontrado! Seu nome � ", end=" ")
                        print(resposta)

        else:
            input("Entrada inv�lida. Pressione Enter")