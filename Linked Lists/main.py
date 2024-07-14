from card import Card
from linked_list import Linked_list

waiting_list = Linked_list()

def inserir():
    """
    Read user input card and, if is valid, insert on the linked list with the correct method
    """
    while True:
        try:
            color_choice = int(input("Insira a cor do cartão: \n1 - Verde\n2 - Amarelo\n0 - Voltar\n"))

            if not color_choice:
                break
            #//TODO: Implements the search with the last number on the list for each color

            number_choice = int(input("Insira um número válido para o cartão:\n"))
            if number_choice < 0:
                print("Valor inválido para cartões\n")
                continue

            if color_choice == 'A':
                if number_choice < 200:
                    print("Valor incorreto para cartões Amarelos\n")
                    continue

        except ValueError:
            print("Valor inserido incorretamente! Tente novamente\n")
            continue

        card = Card(number=number_choice, color=color_choice)

        if not waiting_list.head:
            waiting_list.head = card
            continue
        
        waiting_list.inserirComPrioridade(card) if card.has_priority() else waiting_list.inserirSemPrioridade(card)

def imprimirListaEspera():
    """
    Print the linked list
    """
    print(waiting_list)

inserir()
imprimirListaEspera()