class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i -1
            while((j >=0) and (nums[j] > key)):
                #swap
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
                j-=1
            nums[j+1] = key
        return nums
