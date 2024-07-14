from card import Card
from linked_list import Linked_list

def inserir():
    """
    Read user input card and, if is valid, insert on the linked list with the correct method
    """
    while True:
        try:
            color_choice = input("Insira a cor do cartão: \nV - Verde\nA - Amarelo\nX - Voltar\n").capitalize()
            
            if color_choice == "X":
                break

            if color_choice != "V" and color_choice != "A":
                print("Cor inválida para cartões\n")
                continue

            number_choice = int(input("Insira um número válido para o cartão:\n"))
            if number_choice < 0:
                print("Valor inválido para cartões\n")
                continue

            if color_choice == "A":
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

def atenderPaciente():
    """
    Call patient by the number of card or inform there are no patients
    """
    attend = waiting_list.remove_first_card()
    if not attend:
        return print("Não há nenhum paciente para ser atendido")
    
    print(f"Chamando paciente para atendimento! Número: {attend.number}")

def main():
    print("\nBem vindo ao Sistema de Atendimento\n---> desenvolvido por: Lucas Soares de Abreu")
    print("="*45)

    while True:
        try:
            print("\nEscolha uma das opções:")
            print("1 - Adicionar paciente a fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar Paciente")
            print("4 - Sair")
            action = int(input())

            if action == 1: inserir()
            if action == 2: imprimirListaEspera()
            if action == 3: atenderPaciente()
            
            if action == 4: 
                print("Finalizando...")
                break

        except ValueError:
            print("Valor inserido incorretamente! Tente novamente\n")
            continue

waiting_list = Linked_list()
main()