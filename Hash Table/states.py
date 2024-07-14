class State:
    def __init__(self, acronym: str, name: str) -> None:
        self.sigla = acronym
        self.nomeEstado = name
        self.next = None