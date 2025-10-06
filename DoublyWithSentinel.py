class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


class DoublyLinkedList:
  def __init__(self, value=None):
    if value is None:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      new_node = Node(value)
      self.head = self.tail = new_node
      self.length = 1

  def get_front(self):
    return self.head

  def get_back(self):
    return self.tail

  def push_front(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1

  def push_back(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def pop_front(self):
    if self.length == 0:
      raise IndexError("pop_front() used on empty list")
    value = self.head.value
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
    self.length -= 1
    return value

  def pop_back(self):
    if self.length == 0:
      raise IndexError("pop_back() used on empty list")
    value = self.tail.value
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    self.length -= 1
    return value



class SentinelList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.tail.prev = self.head
    self.head.next = self.tail
    self.length = 0
  def get_front(self):
    return self.head.next if self.length > 0 else None 
  def get_back(self):
    return self.tail.prev if self.length > 0 else None 
  
  def push_back(self, data):
    new_node = Node(data, self.tail, self.tail.prev)
    self.tail.prev.next = new_node
    self.tail.prev= new_node
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
      raise IndexError("pop_back() used on empty list")
    
    temp = self.tail.prev
    temp.prev.next = self.tail
    self.tail.prev = temp.prev

    temp.next = None
    temp.prev = None
    
    self.length -= 1
    return temp.value
  
  