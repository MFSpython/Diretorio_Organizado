import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))


def cria_pasta_move(lista_aquivos):
    os.chdir(pasta_atual)
    pass


def indentificador_diretorio_Atual():

    #lista_aquivos = os.listdir(pasta_atual)
    for (dirpath, dirnames, filenames) in os.walk(pasta_atual):
        if(dirpath == pasta_atual):
            return filenames
        else:
            continue


def main():

    print("\t"+"\033[33m----\033[m"*7)
    print("\t\033[32m |Organizador De Arquivos|\033[m")
    print("\t"+"\033[33m----\033[m"*7)
    print("--> Escolhendo as Opções")
    escolha = str(input("--> Digite A Sua escolho:> "))
    if(escolha == '1'):
        cria_pasta_move(indentificador_diretorio_Atual())
    elif(escolha == '2'):
        pass
    else:
        print("\033[31mEscolha Invalida\033[m")


if __name__ == "__main__":

    main()
