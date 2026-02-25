### 整数反转

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sigh = -1
        else:
            sigh = 1
        x *= sigh
        s = str(x)
        n = len(s)
        i = 0
        chars = []
        while i < n:
            if s[n-1-i] != 0:
                chars.append(s[n-1-i])
            i += 1
        chars = ''.join(chars)
        if ((chars > '2147483647' and sigh == 1) \
            or (chars > '2147483648' and sigh == -1))\
            and len(chars) > 9:
            return 0
        ans = int(chars)
        ans *= sigh
        return ans
