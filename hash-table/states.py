class State:
    def __init__(self, acronym: str, name: str) -> None:
        self.acronym = acronym
        self.name = name
        self.next = None

    def __str__(self) -> str:
        return self.acronym