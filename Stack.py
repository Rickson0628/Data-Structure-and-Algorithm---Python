class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def print_stack(self):
        temp = self.top
        print("Stack (top -> bottom):")
        while temp is not None:
            print(temp.value)
            temp = temp.next
        if self.height == 0:
            print("Stack is empty.")

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.height == 0

    def size(self):
        return self.height

    def to_list(self):
        result = []
        temp = self.top
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result

    def clear(self):
        self.top = None
        self.height = 0



def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop().value
    return reversed_s

def is_balanced_parentheses(s):
    stack = Stack()
    for char in s:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop().value
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop().value)
        sorted_stack.push(temp)
    # Transfer back to original stack
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop().value)
    return stack


# ---------------- Interactive Menu ----------------
def stack_menu():
    stack = Stack()
    while True:
        print("\n=== Stack Menu ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek (top)")
        print("4. Print Stack")
        print("5. Size of Stack")
        print("6. Is Empty?")
        print("7. Reverse a String")
        print("8. Check Balanced Parentheses")
        print("9. Sort Stack")
        print("0. Exit")

        choice = input("Enter your choice (number): ")

        if choice == "1":
            val = input("Enter value to push: ")
            stack.push(val)
            print(f"Pushed {val} onto stack.")

        elif choice == "2":
            popped = stack.pop()
            if popped:
                print(f"Popped: {popped.value}")
            else:
                print("Stack is empty. Nothing to pop.")

        elif choice == "3":
            top_val = stack.peek()
            print(f"Top of stack: {top_val}" if top_val else "Stack is empty.")

        elif choice == "4":
            stack.print_stack()

        elif choice == "5":
            print(f"Stack size: {stack.size()}")

        elif choice == "6":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")

        elif choice == "7":
            s = input("Enter string to reverse: ")
            print("Reversed string:", reverse_string(s))

        elif choice == "8":
            s = input("Enter parentheses string to check: ")
            print("Balanced:" if is_balanced_parentheses(s) else "Not balanced")

        elif choice == "9":
            sort_stack(stack)
            print("Stack sorted (smallest on top).")

        elif choice == "0":
            print("Exiting Stack Menu...")
            break

        else:
            print("Invalid choice. Please try again.")

        cont = input("\nContinue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting Stack Menu...")
            break


if __name__ == "__main__":
    stack_menu()
