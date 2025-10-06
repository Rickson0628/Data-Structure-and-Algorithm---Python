class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return new_node

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return new_node

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # ---------------- Access Methods ----------------

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
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
        prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node
        self.length += 1
        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def is_palindrome(self):
        if self.length <= 1:
            return True
        front = self.head
        back = self.tail
        for _ in range(self.length // 2):
            if front.value == back.value:
                front = front.next
                back = back.prev 
            else:
                return False 
        return True

    def reverse(self):
        if self.length == 0:
            return
        before = None
        current = self.head
        self.tail = self.head
        while current is not None:
            
            current.prev = current.next
            current.next = before
            
            before = current
            current = current.prev
            
        self.head = before
    def partition_list(self, val):
        if self.length == 0:
            return None
        
        less_dummy = Node(0)
        greater_dummy = Node(0)
        less = less_dummy
        greater = greater_dummy
        temp = self.head
  
        while temp:
            next_node = temp.next
            temp.next = None
            temp.prev = None
            
            if temp.value < val:
                less.next = temp
                temp.prev = less
                less = less.next
            
            else: 
                greater.next = temp
                temp.prev = greater 
                greater = greater.next
    
            temp = next_node
         
            
        if less_dummy.next:
            self.head = less_dummy.next
            self.head.prev = None
            self.tail = less
            if greater_dummy.next:
                less.next = greater_dummy.next
                greater_dummy.next.prev = less
                self.tail = greater
        else:
            self.head = greater_dummy.next
            self.head.prev = None
            self.tail = greater
        
    def reverse_between(self, start_index, end_index):

        if self.length <= 1 or start_index == end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy

        prev = dummy
        for _ in range(start_index):
            prev = prev.next

        current = prev.next

        for _ in range(end_index - start_index):
            node_to_move = current.next

            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current

            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev

        self.head = dummy.next
        self.head.prev = None

    def swap_pairs(self):
        if self.length <= 1:
            return
        
        dummy_node = Node(0)
        dummy = dummy_node
        current = self.head
  
        
        while current is not None and current.next is not None:
            
            next_node = current.next
            next_pair = next_node.next
            
            dummy.next = next_node  
            next_node.prev = dummy
            next_node.next = current
            current.prev = next_node
            
           
            if next_pair:
                current.next = next_pair
                next_pair.prev = current
                dummy = current
                current = next_pair
            else: 
                current.next = None
            
        self.head = dummy_node.next
        self.head.prev = None
        self.tail = current


    # ---------------- Helper Methods ----------------

    def print_list(self):
        temp = self.head
        while temp:
            print("Value:", temp.value)
            temp = temp.next

    def __len__(self):
        return self.length

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next


# ---------------- Interactive Menu ----------------
def menu():
    dll = DoublyLinkedList()
    while True:
        print("\n=== Doubly Linked List Menu ===")
        print("1. Append")
        print("2. Prepend")
        print("3. Insert at index")
        print("4. Remove at index")
        print("5. Pop (remove last)")
        print("6. Pop first")
        print("7. Print list")
        print("8. Get value at index")
        print("9. Set value at index")
        print("10. Length of list")
        print("11. Is Palindrome")
        print("12. Reverse")
        print("13. Partition List")
        print("14. Reverse Between")
        print("15. Swap Pairs")
        print("0. Exit")

        choice = input("Enter your choice (using number): ")

        if choice == "1":
            val = int(input("Enter value to append: "))
            dll.append(val)

        elif choice == "2":
            val = int(input("Enter value to prepend: "))
            dll.prepend(val)

        elif choice == "3":
            idx = int(input("Enter index: "))
            val = int(input("Enter value: "))
            dll.insert(idx, val)

        elif choice == "4":
            idx = int(input("Enter index to remove: "))
            removed = dll.remove(idx)
            print("Removed:", removed.value if removed else "None")

        elif choice == "5":
            removed = dll.pop()
            print("Popped:", removed.value if removed else "None")

        elif choice == "6":
            removed = dll.pop_first()
            print("Popped first:", removed.value if removed else "None")

        elif choice == "7":
            dll.print_list()

        elif choice == "8":
            idx = int(input("Enter index: "))
            node = dll.get(idx)
            print("Value:", node.value if node else "None")

        elif choice == "9":
            idx = int(input("Enter index: "))
            val = int(input("Enter new value: "))
            node = dll.set(idx, val)
            print("Updated:", node.value if node else "None")

        elif choice == "10":
            print("Length:", len(dll))

        elif choice == "11":
            print("Is palindrome:", dll.is_palindrome())

        elif choice == "12":
            dll.reverse()
            print("List reversed.")
            dll.print_list()

        elif choice == "13":
            val = int(input("Enter partition value: "))
            dll.partition_list(val)
            print("Partitioned list:")
            dll.print_list()

        elif choice == "14":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            dll.reverse_between(start, end)
            print("List after reversing between indices:")
            dll.print_list()

        elif choice == "15":
            dll.swap_pairs()
            print("List after swapping pairs:")
            dll.print_list()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")

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
