class Solution:
    def ZeroSum(self, Arr):
        # write your method here
        se=set()
        s=0
        for i in range(len(Arr)):
            s+=Arr[i]
            if s==0 or s in se:
                return True
            se.add(s)
        return False
