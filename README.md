# Linked List Implementations in Python

This repository contains multiple **Linked List** and **Doubly Linked List** implementations in Python. It includes standard linked lists, doubly linked lists, and sentinel-based doubly linked lists, with a variety of operations and advanced methods. This project is useful for learning and practicing data structures in Python.

---

## Features

### Singly Linked List
- Core operations: `append`, `prepend`, `insert`, `remove`, `pop`, `pop_first`
- Advanced methods:
  - `reverse()` – Reverse the entire list
  - `swap_pairs()` – Swap every two adjacent nodes
  - `reverse_between(start, end)` – Reverse nodes between given indices
  - `partition_list(x)` – Partition list around a value `x`
  - `binary_to_decimal()` – Convert a binary number stored in the list to decimal
  - `find_middle_node()` – Find the middle node
  - `has_loop()` – Detect if the list has a cycle
  - `remove_duplicates()` – Remove duplicate values
- Supports Pythonic iteration and `len()`

---

### Doubly Linked List
- Nodes have `prev` and `next` pointers
- Core operations: `append`, `prepend`, `insert`, `remove`, `pop`, `pop_first`
- Advanced methods:
  - `reverse()` – Reverse the entire list
  - `swap_pairs()` – Swap every two adjacent nodes
  - `reverse_between(start, end)` – Reverse nodes between indices
  - `partition_list(value)` – Partition the list around a value
  - `is_palindrome()` – Check if the list is a palindrome
- Supports iteration and `len()`
- Includes **interactive menu** for testing all functionalities

---

### Sentinel-based Doubly Linked List
- Uses **sentinel head and tail nodes** to simplify edge cases
- Supports:
  - `push_front`, `push_back`
  - `pop_front`, `pop_back`
  - `get_front`, `get_back`
- Automatically handles empty lists without extra checks

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/linked-list-python.git
cd linked-list-python
