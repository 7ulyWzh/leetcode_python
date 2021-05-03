# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组 
#  👍 480 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[] for i in range(numRows)]
        for row_idx in range(numRows):
            for j in range(row_idx + 1):  # j在[1, row_idx-1]操作；0，row_idx取1
                if j == 0 or j == row_idx:
                    triangle[row_idx] += [1]
                else:
                    triangle[row_idx] += [triangle[row_idx - 1][j - 1] + triangle[row_idx - 1][j]]

        return triangle

s = Solution()
print(s.generate(5))



# leetcode submit region end(Prohibit modification and deletion)
