class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def quickSort(self, nums, low, high):
        if(low < high):
            pivot = self.findPivot(nums, low, high)
            self.quickSort(nums, low, pivot-1)
            self.quickSort(nums, pivot+1, high)
    
    def findPivot(self, nums, low, high):
        pivot = nums[high]
        i = low-1
        for j in range(low, high):
            if(nums[j] < pivot):
                #swap
                i+=1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
        #swap i+1 th element with pivot, to get the pivot for partition
        temp = nums[i+1]
        nums[i+1] = nums[high]
        nums[high] = temp
        return i+1
