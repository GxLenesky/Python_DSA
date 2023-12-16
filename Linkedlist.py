import numpy as np
from collections import deque


class LinkedlistTest:
    def test(self): # Create an Linkedlist
        linkedlist = deque()
        
        # Add element
        # Time Complexity: O(1)
        linkedlist.append(1)
        linkedlist.append(2)
        linkedlist.append(3)
        #[1,2,3]
        print(linkedlist)
        
        # Insert element
        # Time Complexty: O(N)
        linkedlist.insert(2, 99)
        # [1, 2, 99, 3]
        print(linkedlist)
        
        # Access element
        # Time Complexity: O(N)
        element = linkedlist[2]
        #99
        print(element)
        
        # Search element
        # Time Complexity: O(N)
        index = linkedlist.index(99)
        #2
        print(index)
        
        # Update element
        # Time Complexity: O(N)
        linkedlist[2] = 88
        #[1,2,88,3]
        print(linkedlist)
        
        # remove element
        # Time Complexity: O(N)
        linkedlist.remove(88)
        #[1,2,3]
        print(linkedlist)
        
        # Length
        # Time Complexity: O(1)
        length = len(linkedlist)
        #3
        print(length)
        
        
if __name__ == "__main__":
    test = LinkedlistTest()
    test.test()