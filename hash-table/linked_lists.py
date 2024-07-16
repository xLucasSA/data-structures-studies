from states import State

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def __mul__(self, integer: int) -> dict[int, "Linked_list"]:
        """
        Create multiple instances of linked lists
        """
        result = {}

        for i in range(0, integer):
            result[i] = Linked_list()

        return result
    
    def __str__(self) -> str:
        text = ""
        current_state: State = self.head

        while current_state:
            text += f"{current_state} -> "
            current_state = current_state.next 

        text += "None" 
        return text
    
    def insert(self, state: State) -> None:
        """
        Insert new acronym in the linked list. If is empty, insert on linked list's head 
        """
        if not self.head:
            self.head = state
            return

        state.next, self.head = self.head, state