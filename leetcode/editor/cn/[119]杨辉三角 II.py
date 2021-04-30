# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 279 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 重点是优化到 O(k) 空间复杂度
        row = []
        for k in range(rowIndex + 1):
            if k == 0 or k == rowIndex:
                row += [1]
            else:
                row += [int(self.f(rowIndex) / (self.f(k) * self.f(rowIndex - k)))]  # 组合数
        return row

    def f(self, x):
        if x == 0:
            return 1
        return x * self.f(x-1)

s = Solution()
s.getRow(3)
# leetcode submit region end(Prohibit modification and deletion)
