class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        d ={}
        for i in range(len(nums)):
            d[target-nums[i]]=i
        for i in range(len(nums)):
            if nums[i] in d:
                j = d[nums[i]]
                if i==j:
                    continue
                elif i<j:
                    return [i,j]
                else:
                    return [j,i]
        
        