class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class SentinelList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get_front(self):
        return self.head.next if self.length > 0 else None

    def get_back(self):
        return self.tail.prev if self.length > 0 else None

    def push_back(self, data):
        new_node = Node(data, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.length += 1

    def push_front(self, data):
        new_node = Node(data, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            raise IndexError('pop_front() used on empty list')
        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp.value

    def pop_back(self):
        if self.length == 0:
            raise IndexError('pop_back() used on empty list')
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def print_list(self):
        temp = self.head.next
        values = []
        while temp != self.tail:
            values.append(temp.value)
            temp = temp.next
        print("List:", values)

    def to_list(self):
        result = []
        temp = self.head.next
        while temp != self.tail:
            result.append(temp.value)
            temp = temp.next
        return result

    def reverse_list(self):
        if self.length <= 1:
            return
        current = self.head.next
        prev_node = self.head
        self.tail.prev = current
        while current != self.tail:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head.next = prev_node
        self.head.next.prev = self.head
        self.tail.prev.next = self.tail

    def has_loop(self):
        slow = self.head.next
        fast = self.head.next
        while fast != self.tail and fast.next != self.tail:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# ---------------- Interactive Menu ----------------
def sentinel_list_menu():
    slist = SentinelList()
    while True:
        print("\n=== Sentinel List Menu ===")
        print("1. Push Front")
        print("2. Push Back")
        print("3. Pop Front")
        print("4. Pop Back")
        print("5. Print List")
        print("6. Size")
        print("7. Is Empty")
        print("8. Convert to Python List")
        print("9. Reverse List")
        print("10. Check for Loop")
        print("0. Exit")

        choice = input("Enter choice (number): ")

        if choice == "1":
            val = input("Enter value to push front: ")
            slist.push_front(val)

        elif choice == "2":
            val = input("Enter value to push back: ")
            slist.push_back(val)

        elif choice == "3":
            try:
                print("Popped front:", slist.pop_front())
            except IndexError as e:
                print(e)

        elif choice == "4":
            try:
                print("Popped back:", slist.pop_back())
            except IndexError as e:
                print(e)

        elif choice == "5":
            slist.print_list()

        elif choice == "6":
            print("Size:", slist.size())

        elif choice == "7":
            print("Empty?" , slist.is_empty())

        elif choice == "8":
            print("Python list:", slist.to_list())

        elif choice == "9":
            slist.reverse_list()
            print("List reversed.")
            slist.print_list()

        elif choice == "10":
            print("Has loop?", slist.has_loop())

        elif choice == "0":
            print("Exiting Sentinel List Menu...")
            break

        else:
            print("Invalid choice!")

        cont = input("\nContinue? (y/n): ").strip().lower()
        if cont != "y":
            print("Exiting Sentinel List Menu...")
            break

if __name__ == "__main__":
    sentinel_list_menu()
