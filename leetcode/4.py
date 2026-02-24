### 寻找两个正序数组的中位数

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       temp = []
       i = 0
       j = 0
       while(i < len(nums1) and j < len(nums2)):
        if(nums1[i] <= nums2[j]):
            temp.append(nums1[i])
            i += 1
        else:
            temp.append(nums2[j])
            j += 1
       while(i < len(nums1)):
        temp.append(nums1[i])
        i += 1
       while(j < len(nums2)):
        temp.append(nums2[j])
        j += 1
       n = len(temp)
       return (temp[int(n/2)] + temp[int((n - 1)/2)]) / 2.0