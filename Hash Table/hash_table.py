from linked_lists import Linked_list
from states import State

class Hash_table:
    def __init__(self, lists: int) -> None:
        self.table = Linked_list() * lists
    
    def __str__(self) -> str:
        text = ""
        
        for key, value in self.table.items():
            text += f"{key}: {value}\n"
        
        return text
    
    def insert(self, state: State) -> None:
        """
        Insert new State on hash_table generating hash with State acronym. If State is DF insert on index 7
        """
        if state.sigla == "DF":
            self.table[7].insert(state)

        number_hash = (ord(state.sigla[0]) + ord(state.sigla[1])) // 10
        self.table[number_hash].insert(state)
