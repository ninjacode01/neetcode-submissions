class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        seen ={}
        for i, x in enumerate(nums):
            diff = target -x 
            if diff in seen:
                if seen[diff]<i:
                    return [seen[diff],i]
                else:
                    return [i, seen[diff]]
            seen[x] = i
        
        return []
