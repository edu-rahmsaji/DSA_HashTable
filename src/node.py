from __future__ import annotations
from typing import Any, Tuple


class Node:
    def __init__(self, value: Tuple[str, Any | None], prev: Node | None = None, next: Node | None = None) -> None:
        """
        Initializes an element of a linked list.

        Parameters : 
            - value (Tuple[str, Any | None]) : The key-value to store in the node.
            - prev (Node | None) : The reference to the previous node (Optional). Defaults to None.
            - next (Node | None) :The reference to the next node (Optional). Defaults to None.
        """
        self.key: str = value[0]
        self.value: Any = value[1]
        self.prev: Node | None = prev
        self.next: Node | None = next

    def has_prev(self) -> bool:
        """ Checks if the current node references a previous node. """
        return self.prev is not None

    def has_next(self) -> bool:
        """ Checks if the current node references a next node. """
        return self.next is not None
    
    def clone(self):
        """ Deeply clones the current node as a new one, retaining its previous and next node references. """
        return Node((self.key, self.value), self.prev, self.next)
