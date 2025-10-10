class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def print_queue(self):
        temp = self.first
        print("Queue (front -> rear):")
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print() if self.length else print("Queue is empty.")

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        if not self.first:
            self.last = None
        temp.next = None
        self.length -= 1
        return temp

    def peek(self):
        return self.first.value if self.first else None

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length


    def to_list(self):
        result = []
        temp = self.first
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result

    def reverse(self):
        prev = None
        current = self.first
        self.last = self.first
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.first = prev

    def is_palindrome(self):
        values = self.to_list()
        return values == values[::-1]

    def sort_queue(self):
        if self.length <= 1:
            return
        sorted_list = []
        while not self.is_empty():
            temp = self.dequeue().value
            inserted = False
            for i in range(len(sorted_list)):
                if temp < sorted_list[i]:
                    sorted_list.insert(i, temp)
                    inserted = True
                    break
            if not inserted:
                sorted_list.append(temp)
        for val in sorted_list:
            self.enqueue(val)


# ---------------- Interactive Menu ----------------
def queue_menu():
    queue = Queue()
    while True:
        print("\n=== Queue Menu ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek (front)")
        print("4. Print Queue")
        print("5. Size of Queue")
        print("6. Is Empty?")
        print("7. Reverse Queue")
        print("8. Check Palindrome")
        print("9. Sort Queue")
        print("10. Convert to List")
        print("0. Exit")

        choice = input("Enter your choice (number): ")

        if choice == "1":
            val = input("Enter value to enqueue: ")
            queue.enqueue(val)
            print(f"Enqueued {val}.")

        elif choice == "2":
            dequeued = queue.dequeue()
            print(f"Dequeued: {dequeued.value}" if dequeued else "Queue is empty.")

        elif choice == "3":
            front_val = queue.peek()
            print(f"Front of queue: {front_val}" if front_val else "Queue is empty.")

        elif choice == "4":
            queue.print_queue()

        elif choice == "5":
            print(f"Queue size: {queue.size()}")

        elif choice == "6":
            print("Queue is empty." if queue.is_empty() else "Queue is not empty.")

        elif choice == "7":
            queue.reverse()
            print("Queue reversed.")
            queue.print_queue()

        elif choice == "8":
            print("Queue is palindrome." if queue.is_palindrome() else "Queue is not palindrome.")

        elif choice == "9":
            queue.sort_queue()
            print("Queue sorted.")
            queue.print_queue()

        elif choice == "10":
            print("Queue as list:", queue.to_list())

        elif choice == "0":
            print("Exiting Queue Menu...")
            break

        else:
            print("Invalid choice. Try again.")

        cont = input("\nContinue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting Queue Menu...")
            break


if __name__ == "__main__":
    queue_menu()
