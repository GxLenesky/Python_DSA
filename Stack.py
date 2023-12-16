class StackTest:
    def test(self): # Create a stack
        stack =[]
        
        # Add element
        # Time complexity: O(1)
        stack.append(1)
        stack.append(2)
        stack.append(3)
        #1,2,3
        print(stack)
        
        # Get the top of stack
        # Time complexity: O(1)
        stack[-1]
        
        # Remove the top of stack
        # Time compelxity: O(1)
        temp = stack.pop( )
        #3
        print(temp)
        
        # Get stack length
        # Time compelxity: O(1)
        len(stack)
        
        # Stack is empty?
        # Time compelxity: O(1)
        len(stack) == 0
        
        # Iterate Stack
        # Time complexity: 0(N)
        while len(stack) > 0:
            temp = stack.pop()
            print(temp)
