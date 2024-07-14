from linked_lists import Linked_list

class Hash_table:
    def __init__(self, lists: int) -> None:
        self.table = Linked_list() * lists
    
    def __str__(self) -> str:
        text = ""
        
        for key, value in self.table.items():
            text += f"{key}: {value}\n"
        
        return text

print(Hash_table(10))