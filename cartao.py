class Card:
    def __init__(self, number: int, color: str) -> None:
        self.number = number
        self.color = color
        self.next = None

    def __str__(self) -> str:
        return f"{self.number} - {self.color}"