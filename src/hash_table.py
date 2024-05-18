from __future__ import annotations
from typing import Any, List, Tuple
from linked_list import LinkedList

class HashTable:
    def __init__(self, m: int = 12):
        """
        Creates a new hash table.

        Keyword arguments:
        m -- The maximum size of the slots array (default 12)
        """

        self.__m = m
        """ The maximum size of the slots array. """

        self.__slots: List[LinkedList] = [LinkedList() for _ in range(self.__m)]
        """ The slots array containing the linked lists. """

    def contains(self, key: str) -> bool:
        """
        Checks if a given key exists in the hash table.

        Keyword arguments:
        key -- The key to check in the hash table.

        Return :
            - True if the given key exists in the hash table, False otherwise.
        """
        return self.get(key) is not None

    def get(self, key: str, default: Any | None = None) -> Any | None:
        """
        Retrieves the value corresponding with a given key.

        Params :
            - key (str) : The key of the value to get in the hash table.

        Return :
            - The value of the given key if it exists, False otherwise.
        """
        return self.__get_slot(key).get(key, default)

    def put(self, key: str, value: Any, overwrite: bool = True) -> bool:
        """
        Adds a new value with the given key in the hash table.
        If it already exists, the old value is overriden.

        Params :
            - key (str) : The key of the value to add in the hash table.
            - value (Any) : The value to add for the given key in the hash table.

        Return :
            - True if an insertion or an update has occurred, else False
        """
        slot = self.__get_slot(key)

        if slot.get(key) is not None and overwrite:
            return slot.update(key, value)
        elif slot.get(key) is None:
            return slot.insert(key, value)
        
        return False

    def __get_slot(self, key: str) -> LinkedList:
        """ Returns the slot in which the given key is stored. """
        return self.__slots[self.__hash(key)]

    def remove(self, key: str) -> None:
        """
        Removes the value of a given key in the hash table.

        Params :
            - key (str) : The key of the value to remove in the hash table.

        Return :
            - True if the key was removed, False if it wasn't found.
        """
        return self.__get_slot(key).remove(key)

    def size(self) -> int:
        """ Returns the size of the hash table. """
        size = 0

        for slot in self.__slots:
            size += slot.size()

        return size

    def is_empty(self) -> bool:
        """ True if the hash table is empty, False otherwise. """
        return self.size() == 0

    def keys(self) -> List[str]:
        """ Returns the keys of the hash table. """
        keys = []

        for slot in self.__slots:
            keys.extend(slot.keys())

        return keys

    def values(self) -> List[str]:
        """ Returns the values of the hash table. """
        values = []

        for slot in self.__slots:
            values.extend(slot.values())

        return values
    
    def entries(self) -> List[Tuple[str, Any]]:
        """ Returns the key-value pairs of the hash table. """
        entries = []

        for slot in self.__slots:
            entries.extend(slot.entries())

        return entries
    
    def clear(self) -> None:
        """ Clears the hash table. """
        for slot in self.__slots:
            slot.clear()

    def clone(self) -> HashTable:
        """ Clones the current hash table. """
        hash_table = HashTable()
        hash_table.__slots = [slot.clone() for slot in self.__slots]

        return hash_table

    def __hash(self, key: str):
        """
        A static hash function to transform a given key.
        See for reference : https://stackoverflow.com/a/2624210/20892950
        """
        hash = 7;

        for char in key:
            hash = hash * 31 + ord(char.encode("utf-8"))

        return hash % self.__m
