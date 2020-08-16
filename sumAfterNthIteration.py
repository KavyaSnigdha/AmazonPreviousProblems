class Solution:
    def NthIterationSum(self, Arr):
        k=[]
        while len(Arr)>2:
           
            for i in range(len(Arr)-1):
                k.append(Arr[i]-Arr[i+1])
            
            Arr=k
            
            k=[]
        return sum(Arr)    
