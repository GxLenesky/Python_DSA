import numpy as np

class ArrayTest:
    def test(self): # Create an array
        a = []
        # Add element
        # Time Complexity: 0(1)
        
        a.append(1)
        a.append(2)
        a.append(3)    
        
        # [1, 2, 3]
        print(a)
        
        # Insert element
        # Time Complexity: O(N)
        a.insert(2, 99)
        # [1, 2, 99, 3]
        print(a)

        # Access element
        # Time Complexity: O(1)
        temp = a[2]
        #99
        print(temp)

        # Update element
        # Time Complexity: O(1)
        a[2] = 88
        #[1, 2, 88, 3]
        print(a)

        # Remove element
        # Time Complexity: O(N)
        a.remove(88)
        # [1, 2, 3]
        print(a)
        
        a.pop(1)
        # [1,3]
        print(a)
        
        # Time Complexity: O(1)
        a.pop()
        #[1]
        print(a)
        
        
        
a = [1,2,3]
# Get array size
size = len(a)
#3
print(size)

# Iterate array
# Time complexity: 0(N)
for i in a:
    print(i)

for index, element in enumerate(a):
    print("Index at ", index,"is :", element)
    
for i in range(0, len(a)):
    print("i: ", i, "element:", a[i])
    
# Find an element
# Time complexity: O(N)
index = a.index(2)
#1
print(index)

# Sort an array
# Time Complexity: 0(NlogN)
# From small to big
a = [3,1,2]
a.sort()
# [1,2,3]
print(a)
# From big to small
a.sort(reverse = True)
# [3,2,1]
print(a)


if __name__ == "__main__":
    test = ArrayTest()
    test.test()
