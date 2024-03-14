from stack import Stack
from queue import Queue
from linkedList import LinkedList
from bst import BST

def main():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(5)
    print(my_stack.items)
    print(my_stack.pop())
    print(my_stack.items)
    print(my_stack.is_empty())

    my_linked_list = LinkedList()
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(5)
    my_linked_list.append(100)
    my_linked_list.prepend(11)
    my_linked_list.traverse()
    print(my_linked_list.head.value)

    my_bst = BST()
    my_bst.insert(100)

if __name__ == "__main__":
    main()