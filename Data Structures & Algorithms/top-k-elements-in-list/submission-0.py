from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f = [[-c[x],x] for x in c]
        heapq.heapify(f)
        res=[]
        for i in range(k):
            x,y = heapq.heappop(f)
            res.append(y)
        return res



        