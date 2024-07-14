from card import Card

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        text = "Lista -> "
        current_card: Card = self.head

        while current_card:
            text += f"{current_card}, "
            current_card = current_card.next  

        return text

    def inserirSemPrioridade(self, card: Card) -> None:
        """
        Recive one card and insert on the last position of linked list
        """
        if not self.head:
            self.head = card
            return

        current_card: Card = self.head

        while current_card:
            if not current_card.next:
                current_card.next = card
                return

            current_card = current_card.next
        
#     def inserirComPrioridade()

    
# lista = Linked_list()
# cartao1 = Card(1, 'cartao1')
# cartao2 = Card(2, 'cartao2')
# cartao3 = Card(3, 'cartao3')

# lista.inserirSemPrioridade(cartao1)
# lista.inserirSemPrioridade(cartao2)
# lista.inserirSemPrioridade(cartao3)

# print(lista)