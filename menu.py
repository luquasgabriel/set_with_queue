from set_with_queue import SetWithQueue, ElementoDuplicado
from tests import run_tests

def menu_principal():
    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("         Menu Principal             ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1 - Executar SetWithQueue")
        print("2 - Rodar Testes")
        print("3 - Encerrar")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_setwithqueue()
        elif opcao == '2':
            run_tests()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_setwithqueue():
    set_queue = SetWithQueue()

    while True:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("         SetWithQueue()         ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1 - Adicionar elemento")
        print("2 - Remover elemento")
        print("3 - Listar elementos")
        print("4 - Verificar se elemento está no conjunto")
        print("5 - Mostrar tamanho do conjunto")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            elemento = input("Digite o elemento a ser adicionado: ")
            if set_queue.add(elemento):
                print(f"Elemento {elemento} adicionado com sucesso.")
            else:
                print(f"O elemento {elemento} já existe no conjunto.")

        elif opcao == '2':
            elemento = input("Digite o elemento a ser removido: ")
            if set_queue.contains(elemento):
                set_queue.remove(elemento)
                print(f"Elemento {elemento} removido com sucesso.")
            else:
                print(f"O elemento {elemento} não está presente no conjunto")

        elif opcao == '3':
            if set_queue.size() == 0:
                print("Conjunto vazio.")
            print(f"Elementos no conjunto: {set_queue.list()}")

        elif opcao == '4':
            elemento = input("Digite o elemento para verificar: ")
            if set_queue.contains(elemento):
                print(f"O elemento {elemento} está presente.")
            else:
                print(f"O elemento {elemento} não está presente.")

        elif opcao == '5':
            print(f"Tamanho do conjunto: {set_queue.size()}")

        elif opcao == '6':
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
