import heapq

class Test:
    def test(self):
        # Create minheap
        minheap = []
        heapq.heapify(minheap)
        
        # Add element
        heapq.heappush(minheap, 10)
        heapq.heappush(minheap, 8)
        heapq.heappush(minheap, 9)
        heapq.heappush(minheap, 2)
        heapq.heappush(minheap, 1)
        heapq.heappush(minheap, 11)
        #[1，2，9，10，8，11]
        print(minheap)
        
        # peek
        print(minheap[0])
        #1
        
        # Delete
        heapq.heappop(minheap)
        
        #Size
        len(minheap)
        
        
        # Iteration
        while len(minheap)!= 0:
            print(heapq.heappop(minheap))