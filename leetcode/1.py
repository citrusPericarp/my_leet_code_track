### 两数之和

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                # return i, nums.index(target - nums[i])

                # 查哈希表更快，而不是再去查list
                return i, dict[target - nums[i]]