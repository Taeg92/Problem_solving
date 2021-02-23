class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse_bits = format(n, 'b')[::-1]
        reverse_bits += "0" * (32-len(reverse_bits))

        return int(reverse_bits, 2)


n = 4

sol = Solution()

print(sol.reverseBits(n))
