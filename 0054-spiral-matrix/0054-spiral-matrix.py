from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        c_s, c_e = 0, m - 1
        r_s, r_e = 0, n - 1

        ans = []

        while len(ans) < n * m:

            # Left → Right
            for i in range(c_s, c_e + 1):
                ans.append(matrix[r_s][i])
            r_s += 1

            if len(ans) == n * m:
                break

            # Top → Bottom
            for i in range(r_s, r_e + 1):
                ans.append(matrix[i][c_e])
            c_e -= 1

            if len(ans) == n * m:
                break

            # Right → Left
            for i in range(c_e, c_s - 1, -1):
                ans.append(matrix[r_e][i])
            r_e -= 1

            if len(ans) == n * m:
                break

            # Bottom → Top
            for i in range(r_e, r_s - 1, -1):
                ans.append(matrix[i][c_s])
            c_s += 1

        return ans