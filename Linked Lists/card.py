class Card:
    """
    Node of linked list. Contains colors and number of cards, and next element in the linked list
    """
    _color_cards = {
        1: 'V',
        2: 'A'
    }

    def __init__(self, number: int, color: int) -> None:
        self.number = number
        self.color = self._color_cards.get(color)
        self.next = None

    def __str__(self) -> str:
        return f"({self.number}, {self.color})"
    
    def has_priority(self) -> bool:
        return True if self.color == "A" else False 