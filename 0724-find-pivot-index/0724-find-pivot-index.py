class Solution:
    def pivotIndex(self, num: List[int]) -> int:
        total_sum=sum(num)
        left_sum=0
        n=len(num)

        for i in range(n):
            right_sum=total_sum-left_sum-num[i]

            if right_sum==left_sum:
                return i
            else:
                left_sum+=num[i]
        return -1