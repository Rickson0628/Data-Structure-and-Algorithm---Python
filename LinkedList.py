class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    # ---------------- Core Methods ----------------
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        temp = self.head
        for _ in range(self.length - 2):
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.tail
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        return None

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev_node = self.get(index - 1)
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        current = prev.next
        prev.next = current.next
        current.next = None
        self.length -= 1
        return True

    # ---------------- Advanced Methods ----------------
    def print_list(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print("Value:", temp.value)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after
        self.head = prev

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        while current and current.next:
            first = current
            second = current.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next
        self.head = dummy.next

    def reverse_between(self, start, end):
        if self.length <= 1 or start == end:
            return
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(start):
            prev = prev.next
        current = prev.next
        for _ in range(end - start):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next

    def partition_list(self, x):
        less_dummy = Node(0)
        greater_dummy = Node(0)
        less = less_dummy
        greater = greater_dummy
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            if current.value < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = next_node
        less.next = greater_dummy.next
        self.head = less_dummy.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        seen = set()
        prev = None
        current = self.head
        while current:
            if current.value in seen:
                prev.next = current.next
                current.next = None
                self.length -= 1
            else:
                seen.add(current.value)
                prev = current
            current = prev.next if prev else None

    # ---------------- Python Special Methods ----------------
    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


def find_kth_from_end(ll, k):
    fast = ll.head
    slow = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow


# ---------------- Interactive Menu ----------------
def menu():
    ll = LinkedList()

    while True:
        print("\n=== Linked List Menu ===")
        print("1. Append")
        print("2. Prepend")
        print("3. Insert at index")
        print("4. Remove at index")
        print("5. Pop (remove last)")
        print("6. Pop first")
        print("7. Print list")
        print("8. Get value at index")
        print("9. Set value at index")
        print("10. Reverse list")
        print("11. Swap pairs")
        print("12. Reverse between indices")
        print("13. Partition list")
        print("14. Binary to decimal")
        print("15. Get middle node")
        print("16. Check loop")
        print("17. Remove duplicates")
        print("18. Length of list")
        print("19. Iterate list")
        print("20. K-th from end")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            val = int(input("Enter value to append: "))
            ll.append(val)
        elif choice == "2":
            val = int(input("Enter value to prepend: "))
            ll.prepend(val)
        elif choice == "3":
            idx = int(input("Enter index: "))
            val = int(input("Enter value: "))
            ll.insert(idx, val)
        elif choice == "4":
            idx = int(input("Enter index to remove: "))
            ll.remove(idx)
        elif choice == "5":
            ll.pop()
        elif choice == "6":
            ll.pop_first()
        elif choice == "7":
            ll.print_list()
        elif choice == "8":
            idx = int(input("Enter index: "))
            node = ll.get(idx)
            print("Value:", node.value if node else "Invalid index")
        elif choice == "9":
            idx = int(input("Enter index: "))
            val = int(input("Enter value: "))
            ll.set(idx, val)
        elif choice == "10":
            ll.reverse()
        elif choice == "11":
            ll.swap_pairs()
        elif choice == "12":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            ll.reverse_between(start, end)
        elif choice == "13":
            x = int(input("Partition value: "))
            ll.partition_list(x)
        elif choice == "14":
            print("Binary to decimal:", ll.binary_to_decimal())
        elif choice == "15":
            mid = ll.find_middle_node()
            print("Middle node:", mid.value if mid else "Empty list")
        elif choice == "16":
            print("Has loop:", ll.has_loop())
        elif choice == "17":
            ll.remove_duplicates()
        elif choice == "18":
            print("Length:", len(ll))
        elif choice == "19":
            print("Iterating:", [v for v in ll])
        elif choice == "20":
            k = int(input("Enter k: "))
            node = find_kth_from_end(ll, k)
            print("K-th from end:", node.value if node else "Invalid k")
        elif choice == "0":
            break
        else:
            print("Invalid choice")
       
        while True:
            cont = input("\nDo you want to continue? (y/n): ").strip().lower()
            if cont == 'y':
                break 
            elif cont == 'n':
                print("Exiting...")
                return  
            else:
                print("Invalid choice! Only enter 'y' or 'n'.")

if __name__ == "__main__":
    menu()
