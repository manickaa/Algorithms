class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
        swapped = False
        for i in range(0, len(nums)):
            for j in range(0, len(nums)-i-1):
                if(nums[j] > nums[j+1]):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    swapped = True
            if(not swapped):
                break
        return nums
