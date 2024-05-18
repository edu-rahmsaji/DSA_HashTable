from hash_table import HashTable

def main():
    hash_table = HashTable()
    hash_table.put("hello", "world")
    hash_table.put("test", "yo")
    hash_table.put("hey", "dude")
    v = hash_table.clone()
    print(hash_table.size())
    print(hash_table.values())
    print(v.size())
    v.put("last", 1)
    print(hash_table.size())
    print(v.size())
    print(v.values())
        
if __name__ == "__main__":
    main()
