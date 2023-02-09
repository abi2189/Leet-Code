class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sorted= sorted(nums)
        for i in range(len(nums)):
            if i==nums_sorted[i]:
                pass 
            else:
                return i
        return i+1