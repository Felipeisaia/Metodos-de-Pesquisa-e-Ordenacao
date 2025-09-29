class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def __repr__(self):
        return f'Nome: {self.nome}. Idade: {self.idade}'
    

class Ordenacao:
    @staticmethod
    def bolha(lista):
        houve_troca = True
        fim = len(lista)
        while (houve_troca):
            houve_Troca = False
            for i in range (fim - 1):
                if (lista[i].nome > lista[i+1].nome):
                    houve_troca = True
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp
                if (lista[i].nome == lista[i+1].nome):
                    if (lista[i].idade > lista[i+1].idade):
                        houve_troca = True
                        tmp = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = tmp

        fim-=1


def main():
    lista [Pessoa('Alex', 25), Pessoa('Alex', 13), Pessoa('Charles, 13'), Pessoa('Alex', 15), Pessoa('Brian', 23)]


    Ordenacao.bolha(lista)


    for Pessoa in lista:
        print(Pessoa)


if __name__ == '__main__':
    main()