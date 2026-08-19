import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

        #if its size == odd then pop the min heap
        

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap,num)
        elif not self.max_heap:
            if num > self.min_heap[0]:
                prev = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap,prev*-1)
            else:
                heapq.heappush(self.max_heap,num*-1)
        
        #if num is between min heap and max heap
        else:
            if num >= self.max_heap[0]*-1 and num <= self.min_heap[0]:
                heapq.heappush(self.min_heap,num)
            elif num < self.max_heap[0]*-1:
                top = heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap,num*-1)
                heapq.heappush(self.min_heap,top*-1)
            elif num > self.min_heap[0]:
                #top = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap,num)
                #heapq.heappush(self.max_heap,top*-1)
        # print(self.min_heap)
        # print(self.max_heap)
        if len(self.min_heap)>len(self.max_heap)+1:
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,top*-1)
        elif len(self.max_heap) > len(self.min_heap):
            top = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, top*-1)
        

        

    def findMedian(self) -> float:
        if (len(self.min_heap)+len(self.max_heap)) %2==0:
            return float((self.min_heap[0]+ (self.max_heap[0]*-1))/2)
        elif (len(self.min_heap)+len(self.max_heap)) %2 !=0:
            return float(self.min_heap[0])
        
        
        