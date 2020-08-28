class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) == 0):
            return nums
        return self.mergeSort(nums)
        
    
    def mergeSort(self, nums):
        if(len(nums) > 1):
            mid = len(nums) // 2
            leftArray = self.mergeSort(nums[:mid])
            rightArray = self.mergeSort(nums[mid:])
            # print(leftArray, rightArray)
            return self.merge(nums, leftArray, rightArray)
        return nums
    
    def merge(self, nums, leftArray, rightArray):
        
        # print(leftArray, rightArray)
        if(len(leftArray) == 0 and len(rightArray) == 0):
            return []
        elif(len(leftArray) == 0 or len(rightArray) == 0):
            return leftArray + rightArray
        temp = []
        i = j = 0
        while(i < len(leftArray) and j < len(rightArray)):
            
            if(leftArray[i] > rightArray[j]):
                temp.append(rightArray[j])
                j+=1
            elif(leftArray[i] <= rightArray[j]):
                temp.append(leftArray[i])
                i+=1
        while(i < len(leftArray)):
            temp.append(leftArray[i])
            i+=1
        while(j < len(rightArray)):
            temp.append(rightArray[j])
            j+=1
        
        # print(temp)
        return temp
