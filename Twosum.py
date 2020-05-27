class Solution:
    def Two_Sum(self, A, target):
        h = {}
        for i, num in enumerate(A):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
