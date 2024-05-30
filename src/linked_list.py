from __future__ import annotations
from typing import Any, List, Tuple
from node import Node

class LinkedList:
    def __init__(self) -> None:
        """ Initialization of an empty linked list. """
        self.__head: Node | None = None
        self.__tail: Node | None = None

    def insert(self, key: str, value: Any | None) -> None:
        """
        Inserts a new node at the end of the linked list.
        
        Parameters :
            - key (str) : The key of the value to add.
            - value (Any | None) : The value to add in the linked list.
        
        Returns :
            None is returned.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.
            Invariants :
                The linked list is not modified.

        Behavior - The key is of type string :
            Preconditions :
                The key is of type string.
            Postconditions :
                The key-value is inserted in the linked list as the new tail.
                None is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is None")
            
        if type(key) != str:
            raise TypeError("Key is expected to be of type string")
        
        new_node = Node((key, value))
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node # type: ignore[reportOptionalMemberAccess]
            new_node.prev = self.__tail
            self.__tail = new_node

    def update(self, key: str, value: Any | None) -> Any | None:
        """
        Updates a given key with the new value.
        
        Parameters :
            - key (str) : The key of the value to update.
            - value (Any | None) : The new value of the key.
        
        Returns :
            The old value is returned.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.
            Invariants :
                The linked list is not modified.

        Behavior - The key is of type string :
            Preconditions :
                The key is of type string.
            Postconditions :
                The value of the key is updated.
                The old value of the key is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is None")
            
        if type(key) != str:
            raise TypeError("Key is expected to be of type string")
        
        for node in self.__as_list():
            if node.key == key:
                old_value = node.value
                node.value = value
                return old_value
    
    def remove(self, key: str) -> Any | None:
        """
        Removes the key-value corresponding to the given key.
        
        Parameters :
            - key (str) : The key to remove.
        
        Returns :
            If the key exists, the old value is returned. Else, None is returned.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.
            Invariants :
                The linked list is not modified.

        Behavior - The key doesn't exist :
            Preconditions :
                The key doesn't exist in the linked list.
            Postconditions :
                None is returned.
            Invariants :
                The linked list is not modified.

        Behavior - The key exists :
            Preconditions :
                The key exists in the linked list.
            Postconditions :
                The key-value corresponding to the given key is removed from the linked list.
                The old value is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
        
        for node in self.__as_list():
            if node.key == key:
                if node.has_prev() and node.has_next():   # In the middle
                    node.prev.next = node.next # type: ignore[reportOptionalMemberAccess]
                    node.next.prev = node.prev # type: ignore[reportOptionalMemberAccess]
                elif node.has_prev():                    # Last element
                    self.__tail = node.prev
                    self.__tail.next = None # type: ignore[reportOptionalMemberAccess]
                elif node.has_next():                    # First element
                    self.__head = node.next
                    self.__head.prev = None # type: ignore[reportOptionalMemberAccess]
                else:                                   # Only element
                    self.__head = None
                    self.__tail = None

                return node.value

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """
        Retrieves the value with the given key, or a default value if the key doesn't exist.
        
        Parameters :
            - key (str) : The key of the value to retrieve.
            - default (Any | None) : A default value to return if the key doesn't exist (Optional). Defaults to None.
        
        Returns :
            If the key exists, the value of the key is returned. Else, the default value is returned.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.

        Behavior - The key doesn't exist :
            Preconditions :
                The key doesn't exist in the linked list.
            Postconditions :
                If set, the default value is returned, otherwise returns None.

        Behavior - The key exists :
            Preconditions :
                The key exists in the linked list.
            Postconditions :
                The value of given key is returned from the linked list.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
            
        for node in self.__as_list():
            if node.key == key:
                return node.value
            
        return default

    def __as_list(self) -> List[Node]:
        """ Returns the nodes of the linked list as a list. """
        nodes_list: List[Node] = []
        current_node = self.__head

        while current_node is not None:
            nodes_list.append(current_node)
            current_node = current_node.next

        return nodes_list

    def size(self) -> int:
        """ Returns the number of elements inside the linked list. """
        return len(self.__as_list())
    
    def is_empty(self) -> bool:
        """ Checks if the linked list is empty or not. """
        return self.size() == 0
    
    def keys(self) -> List[str]:
        """ Returns the keys of the linked list as a list. """
        keys: List[str] = []

        for node in self.__as_list():
            keys.append(node.key)

        return keys
    
    def values(self) -> List[Any]:
        """ Returns the values of the linked list as a list. """
        values: List[Any] = []

        for node in self.__as_list():
            values.append(node.value)

        return values
    
    def entries(self) -> List[Tuple[str, Any]]:
        """ Returns the key-value pairs of the linked list as a list. """
        entries: List[Tuple[str, Any]] = []

        for node in self.__as_list():
            entries.append((node.key, node.value))

        return entries
    
    def clear(self) -> None:
        """ Clears the linked list. """
        self.__head = None
        self.__tail = None

    def clone(self) -> LinkedList:
        """ Deeply clones the current linked list as a new one. """
        clone = LinkedList()
        
        for node in self.__as_list():
            clone.insert(node.key, node.value)

        return clone
    
    def contains(self, key: str) -> bool:
        """
        Checks if a given key exists in the linked list.
        
        Parameters :
            - key (str) : The key to check.
        
        Returns :
            True if the key exists in the linked list, False otherwise.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.

        Behavior - The key doesn't exist :
            Preconditions :
                The key doesn't exist in the linked list.
            Postconditions :
                False is returned.

        Behavior - The key exists :
            Preconditions :
                The key exists in the linked list.
            Postconditions :
                True is returned.
        """
        for k in self.keys():
            if k == key:
                return True
            
        return False
