class Card:
    """
    Node of linked list. Contains colors and number of cards, and next element in the linked list
    """
    def __init__(self, number: int, color: str) -> None:
        self.number = number
        self.color = color
        self.next = None

    def __str__(self) -> str:
        return f"({self.number}, {self.color})"
    
    def has_priority(self) -> bool:
        return True if self.color == "A" else False