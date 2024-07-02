class Solution:
    def numberOfSteps(self, num: int, count = 0) -> int:
        if num != 0:
            if num % 2 == 0:
                count += 1
                return self.numberOfSteps(num // 2, count)
            else:
                count += 1
                return self.numberOfSteps(num - 1, count)
        return count


sol = Solution()
print(sol.numberOfSteps(8))