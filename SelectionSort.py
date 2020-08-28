class Solution:
	def findMin(self, nums, start, end):
        min, minIndex = nums[start], start
        for i in range(start, end):
            if(nums[i] < min):
                min, minIndex = nums[i], i
        return minIndex
    
    def sortArray(self, nums: List[int]) -> List[int]:
        #selection sort
        for i in range(0, len(nums)):
            start = i
            end = len(nums)
            minIndex = self.findMin(nums, start, end)
            #swap
            if(start != minIndex):
                temp = nums[i]
                nums[i] = nums[minIndex]
                nums[minIndex] = temp
        return nums
