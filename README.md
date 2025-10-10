# Linked List Implementations in Python

This repository contains multiple **Linked List**, **Doubly Linked List**, **Stack**, **Queue**, and **Sentinel-based Doubly Linked List** implementations in Python. It demonstrates a variety of operations and advanced methods, making it a great resource for learning and practicing data structures in Python.

> **Note:** All data structures can be accessed and tested through a single **menu system**. Simply run `menu.py` to interact with all functionalities in one place.

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

### Stack
- Implements stack using **linked nodes**
- Core operations: `push`, `pop`, `peek`
- Advanced features:
  - `reverse_string(string)` – Reverse a string using a stack
  - `is_balanced_parentheses(string)` – Check if parentheses are balanced
  - `sort_stack()` – Sort elements in the stack
- Supports **printing the stack** and tracking **height**

---

### Queue
- Implements queue using **linked nodes** or **two-stack method**
- Core operations: `enqueue`, `dequeue`, `peek`
- Advanced features:
  - `is_empty()` – Check if queue is empty
  - Supports **two-stack method for queue behavior**
- Supports printing the queue and tracking **length**

---

### Sentinel-based Doubly Linked List
- Uses **sentinel head and tail nodes** to simplify edge cases
- Supports:
  - `push_front`, `push_back`
  - `pop_front`, `pop_back`
  - `get_front`, `get_back`
  - `size()`, `is_empty()`, `to_list()`
  - `reverse_list()` – Reverse the entire list
  - `has_loop()` – Detect if the list contains a cycle
- Includes **interactive menu** for testing all functionalities
- Automatically handles empty lists without extra checks

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/linked-list-python.git
cd linked-list-python
