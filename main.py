import os
import shutil

pasta_atual = os.path.dirname(os.path.abspath(__file__))


def cria_pasta():
    lista_arquivos, diretorios = indentificador_diretorio_Atual()
    for arquivo in lista_arquivos:

        arq = os.path.splitext(arquivo)[1][1:].capitalize()
        try:
            if arquivo == __file__:
                print(f"Arquivo {arquivo} ignorado")

            else:
                if arq not in diretorios and arq != "":

                    diretorios.append(arq)
                    os.mkdir(pasta_atual + os.sep + arq)
                    print(f"Criando Pasta \033[32m{arq}\033[m")

                    shutil.move(arquivo, pasta_atual + os.sep + arq)
                    print(
                        f"Movendo \033[33m{arquivo}\033[m Para \033[34m{arq}\033[m")

                elif arq == "":

                       print(f"Este Aquivos \033[31m{arquivo}\033[m nao Possui uma extensao Valida") 
                       
                else:

                    shutil.move(arquivo, pasta_atual + os.sep + arq)
                    print(
                        f"Movendo \033[33m{arquivo}\033[m Para \033[34m{arq}\033[m")
                
        except FileExistsError:
            print(f"Verificar este arquivo ==> {arquivo}")

            '''
            if arq not in diretorios and arq != "" and arquivo.lower() != "main.py":
                os.mkdir(pasta_atual+os.sep+arq)
                print(f"Pasta {arq} foi Criada")

                os.rename(pasta_atual+os.sep+arquivo,
                        pasta_atual+os.sep+arq+arquivo)
                print(
                    f">>\033[34m{arquivo}\033[m Foi Movido Para \033[32m{arq}\033[m")
            else:
                os.rename(pasta_atual+os.sep+arquivo,
                        pasta_atual+os.sep+arq+arquivo)
            '''


def indentificador_diretorio_Atual():
    #lista_aquivos = os.listdir(pasta_atual)
    for (dirpath, dirnames, filenames) in os.walk(pasta_atual):
        if(dirpath == pasta_atual):
            return filenames, dirnames


def main():

    os.system("clear || cls")
    print("\t"+"\033[33m----\033[m"*7)
    print("\t\033[32m |Organizador De Arquivos|\033[m")
    print("\t"+"\033[33m----\033[m"*7)
    print("--> Escolhendo as Opções")
    escolha = str(input("--> Digite A Sua escolho:> "))
    #escolha = '1'
    if(escolha == '1'):
        # cria_pasta_move(indentificador_diretorio_Atual())
        cria_pasta()
    elif(escolha == '2'):
        pass
    else:
        print("\033[31mEscolha Invalida\033[m")
    print("\033[36mFim Do Programa\033[m")


if __name__ == "__main__":

    main()
