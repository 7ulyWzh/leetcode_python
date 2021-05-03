# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 890 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = int((left + right) / 2)
            if target <= nums[mid]:  # 应该把=的判定划分给右边，因为最后要取左边的下标，若相等时让左边继续变化即错误
                right = mid - 1
            else:
                left = mid + 1

        return left


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.searchInsert([1,2,3,4],5))