class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1
            n = n >> 1
            res = res | bit
            res = res << 1
        return res >> 1