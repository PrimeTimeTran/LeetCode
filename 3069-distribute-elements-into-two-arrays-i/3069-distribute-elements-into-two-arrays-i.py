class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        print(arr1)
        print(arr2)
        for i in range(0, len(nums)):
            n = nums[i]
            if i == 0:
                arr1.append(n)
            elif i == 1:
                arr2.append(n)
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(n)
                else:
                    arr2.append(n)
        return arr1 + arr2
            