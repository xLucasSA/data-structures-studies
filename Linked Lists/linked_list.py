from card import Card

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        text = "Lista -> "
        current_card: Card = self.head

        while current_card:
            text += f"{current_card} -> "
            current_card = current_card.next  

        text += "None"
        return text

    def inserirSemPrioridade(self, card: Card) -> None:
        """
        Recive one card and insert on the tail of linked list
        """
        current_card: Card = self.head

        while current_card:
            if not current_card.next:
                current_card.next = card
                return

            current_card = current_card.next
        
    def inserirComPrioridade(self, card: Card) -> None:
        """
        Recive one card and insert after all yellow cards. If the linked list don't have any yellow cars, insert on the top
        """    
        current_card: Card = self.head
        if not current_card.has_priority():
            self.head, card.next = card, self.head
            return

        last_yellow_card: Card = None

        while current_card:
            if current_card.has_priority():
                last_yellow_card = current_card
            current_card = current_card.next
        
        last_yellow_card.next, card.next = card, last_yellow_card.next