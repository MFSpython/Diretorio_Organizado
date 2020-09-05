import os



def criar_pasta_local():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    #lista_aquivos = os.listdir(pasta_atual)
    for (dirpath, dirnames, filenames) in os.walk(pasta_atual):
        print(filenames)
  


if __name__ == "__main__":

    print("\t"+"\033[33m----\033[m"*7)
    print("\t\033[32m |Organizador De Arquivos|\033[m")
    print("\t"+"\033[33m----\033[m"*7)
    print("--> Escolhendo as Opções")
    escolha = str(input("--> Digite A Sua escolho:> "))
    if(escolha == '1'):
        criar_pasta_local()
    elif(escolha == '2'):
        pass
    else:
        print("\033[31mEscolha Invalida\033[m")