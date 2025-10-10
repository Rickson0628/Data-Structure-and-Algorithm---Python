from Stack import stack_menu
from Queue import queue_menu
from LinkedList import menu as sll_menu
from DoublyLinkedList import menu as dll_menu
from DoublyWithSentinel import sentinel_list_menu

def main_menu():
    while True:
        print("\n=== Main Data Structures Menu ===")
        print("1. Single Linked List")
        print("2. Doubly Linked List")
        print("3. Doubly Linked List with Sentinel")
        print("4. Queue")
        print("5. Stack")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sll_menu()
        elif choice == "2":
            dll_menu()
        elif choice == "3":
            sentinel_list_menu()
        elif choice == "4":
            queue_menu()
        elif choice == "5":
            stack_menu()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
