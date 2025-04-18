class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low =0 
        high = len(arr) -1 

        while(low<high):
            mid = low + (high - low)//2
            if(arr[mid] < arr[mid-1]):
                high = mid 
            elif(arr[mid]<arr[mid+1]):
                low = mid +1
            else:
                return mid