from dataclasses import dataclass
from typing import List, Any, Optional

@dataclass
class HashTable:
    table_size: int                                         # Initial hash table size

    def __post_init__(self) -> None:
        self.hash_table: List = [None]*self.table_size      # Hash table
        self.num_items: int = 0                             # Empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled, 
        and then incremented to next prime value)."""
        index = self.horner_hash(key)
        j = 0
        while self.hash_table[index] is not None and self.hash_table[index][0] != key:
            index = (index + j**2) % self.table_size
            j += 1
        self.hash_table[index] = (key, value)
        self.num_items += 1
        if self.get_load_factor() > 0.5:
            originalHashKeys = self.get_all_keys()
            originalValues = [self.get_value(i) for i in originalHashKeys]
            originalSize = self.table_size
            n = self.table_size * 2
            while self.isPrime(n) == False:
                n += 1
            self.table_size = n
            newHashTable = [None] * self.table_size
            for i in range(len(originalHashKeys)):
                newIndex = self.horner_hash(originalHashKeys[i])
                newJ = 0
                while newHashTable[newIndex] is not None:
                    newIndex = self.horner_hash(originalHashKeys[i])
                    newJ += 1
                newHashTable[newIndex] = (originalHashKeys[i], originalValues[i])
            self.hash_table = newHashTable

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                print("running")
                return False
        return True


    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        n = min(len(key), 8)
        h = 0
        for i in range(n):
            h += ord(key[i]) * (31 ** (n - 1 - i))
        hashValue = h % self.table_size
        return hashValue

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        hashValue = self.horner_hash(key)
        index = hashValue % self.table_size
        j = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return True
            index = (index + j ** 2) % self.table_size
            j += 1
        return False

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        hashValue = self.horner_hash(key)
        index = hashValue % self.table_size
        j = 0
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return index
            index = (index + j ** 2) % self.table_size
            j += 1
        return None


    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        keys = []
        for i in range(self.table_size):
            if self.hash_table[i] != None:
                keys.append(self.hash_table[i][0])
        return keys

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        index = self.get_index(key)
        if index is not None:
            return self.hash_table[index][1]
        else:
            return None


    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        loadFactor = self.num_items / self.table_size
        return loadFactor

def hashCalculator(key: str) -> int:
    """ Compute and return an integer from 0 to the (size of the hash table) - 1
    Compute the hash value by using Horner’s rule, as described in project specification."""
    n = min(len(key), 8)
    h = 0
    for i in range(n):
        h += ord(key[i]) * (31 ** (n - 1 - i))
        hashValue = h % 7
    return hashValue

t1 = hashCalculator("cat")
t2 = hashCalculator("dog")
t3 = hashCalculator("elephant")
t4 = hashCalculator("mouse")
print(t1, " ", t2, " ", t3, " ",t4)