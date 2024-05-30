from linked_list import LinkedList

def main():
    ll = LinkedList()
    ll.insert("sajidur", "rahman")
    ll.insert("gabriel", "vannay")
    ll.insert("leny", "bressoud")
    print(ll.entries())
    print(ll.get("diogo"))

if __name__ == "__main__":
    main()
