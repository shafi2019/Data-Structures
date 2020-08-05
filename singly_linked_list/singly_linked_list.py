# class Node:
#     def __init__(self, value=None, next_node=None):
#         # the value at this linked list node
#         self.value = value
#         # reference to the next node in the list
#         self.next_node = next_node
#     def get_value(self):
#         return self.value
#     def get_next(self):
#         return self.next_node
#     def set_next(self, new_next):
#         # set this node's next_node reference to the passed in node
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.lenght = 0
    
#  #   def get_length(self):
    
#     def add_to_head(self, value):       
#         new_node = Node(value, self.head)
#         self.head = new_node
#         if  self.lenght == 0:
#             self.tail = new_node
#         self.lenght += 1
    
#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.head is None and self.tail is None:
#             self.head = new_node
#         else:
#             self.tail.set_next(new_node)
#         self.tail = new_node
#         self.lenght += 1
    
#     def remove_head(self):
#         if self.head is None:
#            return None
#         elif self.head == self.tail:
#             value = self.head.get_value()
#             self.head = None
#             self.tail = None
#             self.lenght -= 1
#             return value
#         else:
#             value = self.head.get_value()
#             self.head = self.head.get_next()
#             self.lenght -= 1
#             return value
            
#     def remove_tail(self):
#         if self.head is None:
#             return None
#         elif self.head == self.tail:
#             value = self.tail.get_value()
#             self.head = None
#             self.tail = None
#             self.lenght -= 1
#             return value
#         else:
#             cur_node = self.head
#             while cur_node.get_next() is not self.tail:
#                 cur_node = cur_node.get_next()
#             value = self.tail.get_value()
#             cur_node.set_next(None)
#             self.tail = cur_node
#             self.length -= 1
#             return value

#     def contains(self, value):
#         cur_node = self.head
#         while cur_node is not None:
#             if value == cur_node.get_value():
#                 return True
#             cur_node = cur_node.get_next()
#         return False


#     def get_max(self):
#         if self.head is None:
#             return None
#         cur_node = self.head
#         cur_max = self.head.get_value()
#         while cur_node is not None:
#             if cur_node.get_value() > cur_max:
#                cur_max = cur_node.get_value
#             cur_node = cur_node.get_next()
        
#         return cur_max

    
#     def find_middle(self):
#         mid_point = self.head
#         end_point = self.head
#         while end_point is not None or end_point.next_node() is not None:
#             print("test")
#             mid_point = mid_point.get_next()
#             end_point = end_point.get_next().get_next()

#         return mid_point.value


# ll = LinkedList()
# ll.add_to_tail(1)
# ll.add_to_tail(2)
# ll.add_to_tail(3)
# ll.add_to_tail(4)
# ll.add_to_tail(5)
# print(add_to_tail)

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None

        removed_value = self.head.get_value()
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_value

    def remove_tail(self):
        if not self.head:
            return None

        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()

        prev.set_next(None)
        self.tail = prev
        return curr

    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            curr = curr.get_next()
        return max_value

    def contains(self, value):
        curr = self.head
        while curr != None:
            if curr.get_value() is value:
                return True
            curr = curr.get_next()
        return False 

    
