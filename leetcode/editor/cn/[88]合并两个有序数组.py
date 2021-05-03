# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nu
# ms2 的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -109 <= nums1[i], nums2[i] <= 109 
#  
#  Related Topics 数组 双指针 
#  👍 925 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for idx, num2 in enumerate(nums2):

            left = 0
            right = m + idx - 1  # 右边的位置随着插入数字后+1

            while left <= right:
                mid = int((left + right) / 2)
                if nums1[mid] >= num2:
                    right = mid - 1
                else:
                    left = mid + 1

            for i in range(len(nums1) - 1, left, -1):  # 从要插入的索引+1处开始
                nums1[i] = nums1[i - 1]

            nums1[left] = num2


s = Solution()
nums11 = [1,2,3,0,0,0]

s.merge(nums1 = nums11, m = 3, nums2 = [2,5,6], n = 3)

print(nums11)
# leetcode submit region end(Prohibit modification and deletion)
