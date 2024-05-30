from __future__ import annotations
from typing import Any, Callable, List, Tuple
from linked_list import LinkedList


class HashTable:
    def __init__(self, capacity: int = 12, custom_hash: Callable[[str], int] | None = None):
        """
        Initialized a new empty hash table.

        Parameters :
            - capacity (int) : The size of the slots list (Optional). Default to 12.
            - custom_hash (HashFunction | None) : A custom hash to use instead of the default one (Optional). Defaults to None.
        """
        self.__capacity = capacity
        self.__slots: List[LinkedList] = [LinkedList() for _ in range(self.__capacity)]
        self.__hash: Callable[[str], int] = custom_hash if custom_hash is not None else self.__default_hash

    def contains(self, key: str) -> bool:
        """
        Checks if a given key exists in the hash table.
        
        Parameters :
            - key (str) : The key to check.
        
        Returns :
            True if the key exists in the hash table, False otherwise.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.

        Behavior - The key doesn't exist :
            Preconditions :
                The key doesn't exist in the hash table.
            Postconditions :
                False is returned.

        Behavior - The key exists :
            Preconditions :
                The key exists in the hash table.
            Postconditions :
                True is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
        
        return self.__get_slot(key).contains(key)

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
                The key doesn't exist in the hash table.
            Postconditions :
                If set, the default value is returned, otherwise returns None.

        Behavior - The key exists :
            Preconditions :
                The key exists in the hash table.
            Postconditions :
                The value of given key is returned from the hash table.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
        
        return self.__get_slot(key).get(key, default)

    def put(self, key: str, value: Any | None, override: bool = True) -> Any | None:
        """
         Adds a new value with the given key in the hash table.
        
        Parameters :
            - key (str) : The key of the value to add.
            - value (Any | None) : The value to add in the linked list.
            - override (bool) : If the value should be overriden if the key already exists.
        
        Returns :
            If the key doesn't exist or it exists and override is True, the old value is returned. Else, None is returned.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.
            Invariants :
                The hash table is not modified.

        Behavior - The key doesn't exist :
            Preconditions :
                The key is of type string.
            Postconditions :
                The key-value is inserted in the hash table.
                None is returned.

        Behavior - The key doesn't exist and override is False :
            Preconditions :
                The key is of type string.
                The override parameter is False.
            Postconditions :
                None is returned.
            Invariants :
                The hash table is not modified.

        Behavior - The key doesn't exist and override is True :
            Preconditions :
                The key is of type string.
                The override parameter is True.
            Postconditions :
                The value of the key is updated in the hash table
                The old value is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")

        slot = self.__get_slot(key)

        if slot.get(key) is not None and override:
            return slot.update(key, value)
        elif slot.get(key) is None:
            return slot.insert(key, value)
        
        return False

    def __get_slot(self, key: str) -> LinkedList:
        """
        Retrieves the slot in which the given key is stored.
        
        Parameters :
            - key (str) : The key whose slot to retrieve.
        
        Returns :
            The slot in which the key is stored.
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.

        Behavior - The key is of type string :
            Preconditions :
                The key is of type string.
            Postconditions :
                The slot in which the key is stored is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
        
        return self.__slots[self.__hash(key)]

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
                The hash table is not modified.

        Behavior - The key doesn't exist :
            Preconditions :
                The key doesn't exist in the hash table.
            Postconditions :
                None is returned.
            Invariants :
                The hash table is not modified.

        Behavior - The key exists :
            Preconditions :
                The key exists in the hash table.
            Postconditions :
                The key-value corresponding to the given key is removed from the hash table.
                The old value is returned.
        """
        if key is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Key is expected to be of type string, None received.")
        
        if type(key) != str:
            raise TypeError("Key is expected to be of type string.")
        
        return self.__get_slot(key).remove(key)

    def size(self) -> int:
        """ Returns the number of elements inside the hash table. """
        size = 0

        for slot in self.__slots:
            size += slot.size()

        return size

    def is_empty(self) -> bool:
        """ Checks if the hash table is empty or not. """
        return self.size() == 0

    def keys(self) -> List[str]:
        """ Returns the keys of the hash table as a list. """
        keys: List[str] = []

        for slot in self.__slots:
            keys.extend(slot.keys())

        return keys

    def values(self) -> List[Any]:
        """ Returns the values of the hash table as a list. """
        values: List[Any] = []

        for slot in self.__slots:
            values.extend(slot.values())

        return values
    
    def entries(self) -> List[Tuple[str, Any]]:
        """ Returns the key-value pairs of the hash table as a list. """
        entries: List[Tuple[str, Any]] = []

        for slot in self.__slots:
            entries.extend(slot.entries())

        return entries
    
    def clear(self) -> None:
        """ Clears the hash table. """
        for slot in self.__slots:
            slot.clear()

    def clone(self) -> HashTable:
        """ Deeply clones the current hash table. """
        hash_table = HashTable()
        hash_table.__slots = [slot.clone() for slot in self.__slots]

        return hash_table
    
    def load_factor(self) -> float:
        """ Returns the load factor of the hash table. """
        return self.size() / self.__capacity
    
    def average_slot_distribution(self) -> float:
        """ Returns the average slot distribution of the hash table. """
        total_elements = 0
        non_empty_slots = 0

        for slot in self.__slots:
            if not slot.is_empty():
                total_elements += slot.size()
                non_empty_slots += 1

        return total_elements / non_empty_slots
    
    def get_capacity(self) -> int:
        """ Returns the capacity of the hash table. """
        return self.__capacity
    
    def merge(self, hash_table: HashTable, override: bool = False) -> None:
        """
        Merges the given hash table's values with the current one.
        
        Parameters :
            - hash_table (HashTable) : The hash table whose values to add in the current one.
            - override (bool) : If the value should be overriden if the key already exists (Optional). Defaults to False.
            
        Behavior - The key is not of type hash table :
            Preconditions :
                The key is not of type hash table.
            Postconditions :
                A type error is raised.
            Invariants:
                The current hash table is not modified.

        Behavior - The key is of type hash table :
            Preconditions :
                The key is of type hash table
            Postconditions :
                All the values in the given hash table are added inside the current one.
                None is returned.
        """
        if hash_table is None: # type: ignore[reportOptionalMemberAccess]
            raise TypeError("Hash table is expected to be of type HashTable, None received.")
        
        if type(hash_table) != HashTable:
            raise TypeError("Hash table is expected to be of type HashTable.")
        
        for key, value in hash_table.entries():
            self.put(key, value, override)

    def __default_hash(self, key: str) -> int:
        """
        A static hash function to transform a given key into a valid index for the slots.
        
        Parameters :
            - key (str) : The key to hash.
        
        Returns :
            The hashed value of the key.

        References :
            - https://stackoverflow.com/a/2624210/20892950
            
        Behavior - The key is not of type string :
            Preconditions :
                The key is not of type string.
            Postconditions :
                A type error is raised.

        Behavior - The key is valid :
            Preconditions :
                The key is valid.
            Postconditions :
                The hashed value of the key is returned.
        """
        hash = 7

        for char in key:
            hash = hash * 31 + ord(char.encode("utf-8"))

        return hash % self.__capacity
