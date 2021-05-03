# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：3 
# 
#  示例 2： 
# 
#  
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#  
# 
#  
# 
#  进阶： 
# 
#  
#  尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。 
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 963 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_element = self.majorityElementRec(nums, 0, len(nums) - 1)
        return maj_element

        # 分治法
        # 长度为1：直接返回数字
        # 长度不为1：
            # 递归调用，得到左右两个子数组的众数
            # 比较左右两个子数组的众数是否相等，相等：
                # 返回该众数
            # 不相等：
                # 比较左右两个子数组的众数，在原数组中的出现次数，返回出现次数更多的，即为原数组的众数

    def majorityElementRec(self,nums, low, high):

        if low == high:
            return nums[low]
        else:
            mid = (low + high) // 2
            left = mid  # 左子数组的最大索引
            right = mid + 1  # 右子数组的最小索引
            left_maj_element = self.majorityElementRec(nums, low, left)
            right_maj_element = self.majorityElementRec(nums, right, high)

            if left_maj_element == right_maj_element:
                return left_maj_element

            else:
                left_maj_element_count = [1 for i in range(low, high + 1) if nums[i] == left_maj_element]  # high+1是为了能取到最后一个索引处
                right_maj_element_count = [1 for i in range(low, high + 1) if nums[i] == right_maj_element]
                if left_maj_element_count > right_maj_element_count:
                    return left_maj_element
                else:
                    return right_maj_element


s = Solution()
print(s.majorityElement([3,3,4]))














# leetcode submit region end(Prohibit modification and deletion)
