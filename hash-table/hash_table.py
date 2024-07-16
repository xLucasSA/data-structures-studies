from linked_lists import Linked_list
from states import State

class Hash_table:
    def __init__(self, lists: int) -> None:
        self.data = Linked_list() * lists
    
    def __str__(self) -> str:
        text = ""
        
        for key, value in self.data.items():
            text += f"{key}: {value}\n"
        
        return text
    
    def insert(self, state: State) -> None:
        """
        Insert new State on hash_table generating hash with State acronym. If State is DF insert on index 7
        """
        if state.acronym == "DF":
            self.data[7].insert(state)
            return

        number_hash = (ord(state.acronym[0]) + ord(state.acronym[1])) % 10
        self.data[number_hash].insert(state)
