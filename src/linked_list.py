from __future__ import annotations
from typing import Any, List, Tuple

class LinkedList:
    def __init__(self) -> None:
        """ A linked list. """
        self.__head: Node | None = None
        self.__tail: Node | None = None

    def insert(self, key: str, value: Any) -> bool:
        """ Inserts a new node at the end of the linked list. """
        if self.__head is None:
            self.__head = Node(key, value)
            self.__tail = self.__head
        else:
            lastTail = self.__tail
            self.__tail = Node(key, value, lastTail)
            lastTail.next = self.__tail

        return True

    def update(self, key: str, value: Any) -> bool:
        """ Updates a given key with the new value if found and returns True, otherwise returns False. """
        for node in self.__as_iterable():
            if node.key == key:
                node.value = value
                return True
        
        return False
    
    def remove(self, key: str) -> bool:
        """
        Removes a node containing the given key.

        Returns:
            - True if a node with the given key was found and removed, otherwise False.
        """
        for node in self.__as_iterable():
            if node.key == key:
                if node.hasPrev() and node.hasNext():   # In the middle
                    node.prev.next = node.next
                    node.next.prev = node.prev
                elif node.hasPrev():                    # Last element
                    self.__tail = node.prev
                    self.__tail.next = None
                elif node.hasNext():                    # First element
                    self.__head = node.next
                    self.__head.prev = None
                else:                                   # Only element
                    self.__head = None
                    self.__tail = None

                del node
                return True

        return False    

    def get(self, key: str, default: Any = None) -> Any | None:
        """
        Returns the value with the given key, or a default value if the key doesn't exist.
        """
        for node in self.__as_iterable():
            if node.key == key:
                return node.value
            
        return default

    def __as_iterable(self) -> List[Node]:
        """ Returns the nodes as a list. """
        iterable: List[Node] = []

        if self.__head is not None:
            lastNode = self.__head

            while lastNode.hasNext():
                lastNode = lastNode.next
                iterable.append(lastNode)
            else:
                # Last node was not added
                iterable.append(lastNode)

        return iterable

    def size(self) -> int:
        """ Returns the number of elements inside the linked list. """
        return len(self.__as_iterable())
    
    def keys(self) -> List[str]:
        """ Returns the keys of the linked list. """
        keys = []

        for node in self.__as_iterable():
            keys.append(node.key)

        return keys
    
    def values(self) -> List[Any]:
        """ Returns the values of the linked list. """
        values = []

        for node in self.__as_iterable():
            values.append(node.value)

        return values
    
    def entries(self) -> List[Tuple[str, Any]]:
        """ Returns the key-value pairs of the linked list. """
        entries = []

        for node in self.__as_iterable():
            entries.append([node.key, node.value])

        return entries
    
    def clear(self) -> None:
        """ Clears the linked list. """
        self.__head = None
        self.__tail = None

        for node in self.__as_iterable():
            del node

    def clone(self) -> LinkedList:
        """ Clones the current linked list. """
        clone = LinkedList()
        
        for node in self.__as_iterable():
            clone.insert(node.key, node.value)

        return clone

class Node:
    def __init__(self, key: str, value: Any | None, prev: Node | None = None, next: Node | None = None) -> None:
        """ An element of a linked list. """
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def hasPrev(self) -> bool:
        """ Checks if the current node references a previous node. """
        return self.prev is not None

    def hasNext(self) -> bool:
        """ Checks if the current node references a next node. """
        return self.next is not None
