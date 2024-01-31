class SetTest:
    def test(self):
        # Create Set
        s = set()
        
        # Add element
        # Time Complexity: O(1) 
        s.add(10)
        s.add(3)
        s.add(5)
        s.add(2)
        s.add(2)
        # {2,10,3,5}
        print(s)
        
        # Search Element
        # Time Complexity: O(1)
        2 in s
        
        # Delete Element
        # Time Complexity: O(1)
        s.remove(2)
        print(s)
        
        # Size
        # TimeComplexity: O(1)
        len(s)
