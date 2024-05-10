import os
import random

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.position = 0
        self.length = 1

    def insert_at_end(self, value):
        # Create a node
        new_node = Node(value)

        # If we are the first node, we are the HEAD
        # Otherwise, we are a child node of the head
        if not self.head:
            self.head = new_node
            self.current = self.head
            return
        else:
            # First set the current node's next to the new node
            # Then set the current node to the new node
            self.current.next = new_node
            self.current = self.current.next

        self.length += 1

    def delete_element_at(self, element):
        if element > self.length:
            print(f'Error Length is {self.length}')
            return
        elif element < 0:
            print('Element cannot be less than 0')
            return

        count = 0
        current = self.head

        # Loop through the list and set the next for previous to current.next.next
        while (current is not None):
            # Process for the head of the list
            if element == 0:
                self.head = current.next
                break
            # Loop until we find the element to be deleted
            elif count < element:
                previous = current
                current = current.next
                count += 1
            # Then set the next pointer for the current-1 to the current + 1
            else:
                previous.next = current.next
                break
        # Adjust the length of the list
        self.length -= 1
        # and free up the memory for the deleted object
        del current

    # Reverse the list
    def reverse_elements(self):

        previous = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def swap(self, ptr1, ptr2):
        tmp = ptr2.value
        ptr2.value = ptr1.value
        ptr1.value = tmp

    def bubbleSort(self):
        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.value > current.next.value:
                    self.swap(current, current.next)
                    swapped = True
                current = current.next

    # Print the linked list
    def __repr__(self):
        return_string = ''
        current = self.head
        while current:
            if current == None:
                break
            return_string = return_string + str(current.value) + os.linesep
            current = current.next
        return return_string + f'Number of elements: {len(self)}'

    def __len__(self):
        return self.length


# Creating a linked list
my_list = LinkedList()
my_list.insert_at_end(5)
my_list.insert_at_end(10)
my_list.insert_at_end(15)
my_list.insert_at_end(20)
my_list.insert_at_end(25)
my_list.insert_at_end(30)


print('List elements start at 0')
print(my_list)
print('Deleting Element at 0')
my_list.delete_element_at(0)
print(my_list)

print('Deleting list element 3')
my_list.delete_element_at(3)
print(my_list)

print('Adding elements to list')
my_list.insert_at_end(35)
my_list.insert_at_end(40)
my_list.insert_at_end(45)
my_list.insert_at_end(50)
print(my_list)

print('Reverse the list')
my_list.reverse_elements()
print(my_list)
print('Reverse the list')
my_list.reverse_elements()
print(my_list)

# Sort list
del my_list
my_list = LinkedList()
print('Bubble Sorting a List')

for i in range(0,10):
    my_list.insert_at_end(random.randrange(0,1000))
print("List before sort")
print(my_list)

print('List after sort')
my_list.bubbleSort()
print(my_list)
