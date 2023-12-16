from collections import deque

class QueueTest:
    def test(self):
        # Create a queue
        queue = deque()
        
        # Add element
        # Time Complexity: O(1)
        queue.append(1)
        queue.append(2)
        queue.append(3)
        # [1,2,3]
        print(queue)
    
        # Get the head of the queue
        # Time Complexity: O(1)
        templ = queue[0]
        print(templ)

        # Remove the head of the queue
        # Time Complexity: O(1)
        temp2 = queue.popleft( )
        print(temp2)
        #[2, 3]
        print(queue)
        
        # Queue is empty?
        # Time Complexity: O(1)
        len(queue) == 0
        
        # The length of queue
        # Time Complexity: O(1)
        len(queue)
        
        # Time Complexity: 0(N)
        while len(queue) != 0:
            temp = queue.popleft()
            print(temp)
