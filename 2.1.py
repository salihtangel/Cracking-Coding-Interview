# R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints: #9, #40

from linkled_list import LinkedList

my_linkedlist = LinkedList()
my_linkedlist.append(10)
my_linkedlist.append(10)
my_linkedlist.append(20)
my_linkedlist.append(10)


def remove_duplicates_with_two_pointer(my_linkedlist):
    pointer1 = my_linkedlist.get_head()
    pointer2 = my_linkedlist.get_head() 
    pointer2 = pointer2.next
    current = my_linkedlist.get_head()
    while pointer2 is not None:
        if pointer1.data == pointer2.data:
            deleteNode(pointer1)
        
        current = current.next  


    return my_linkedlist


remove_duplicates_with_two_pointer(my_linkedlist)
my_linkedlist.display()
