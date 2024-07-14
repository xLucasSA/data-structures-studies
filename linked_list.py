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
        Recive one card and insert on the tail of linked list
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
        
    def inserirComPrioridade(self, card: Card) -> None:
        """
        Recive one card and insert after all card with color yellow
        """
        if not self.head:
            self.head = card
            return
        
        current_card: Card = self.head
        last_yellow_card: Card = None

        while current_card:
            if current_card.color == "A":
                last_yellow_card = current_card
            current_card = current_card.next
        
        last_yellow_card.next, card.next = card, last_yellow_card.next

    
# lista = Linked_list()
# cartao1 = Card(1, 'A')
# cartao2 = Card(2, 'V')
# cartao3 = Card(3, 'V')
# cartao4 = Card(4, 'V')

# lista.inserirSemPrioridade(cartao2)
# lista.inserirSemPrioridade(cartao1)
# lista.inserirSemPrioridade(cartao3)
# lista.inserirComPrioridade(cartao4)

# print(lista)