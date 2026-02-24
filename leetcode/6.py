### Z 字形变换

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        chars = []
        if numRows == 1:
            return s

        # 补丁：第0行
        k = 0
        step = 2*numRows - 2
        while k < n:
            chars.append(s[k])
            k += step

        # 第0到 numRows 行
        for i in range(1, numRows - 1):
            step = 2 * numRows - 2 - 2 * i
            k = i
            while k < n:
                chars.append(s[k])
                k += step
                step = 2 * numRows - 2 - step
                
        # 补丁：第 numRows 行
        k = numRows - 1
        step = 2*numRows - 2
        while k < n:
            chars.append(s[k])
            k += step
        return ''.join(chars)