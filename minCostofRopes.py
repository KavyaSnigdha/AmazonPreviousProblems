class Solution:
    def minCost(self, A):
        A=sorted(A)
        
        cost=[]
        k=0
        i=0

        while(i<len(A)-1):   
            A.insert(i,A[i]+A[i+1])
            cost.append(A[i])
            A.pop(i+1)
            A.pop(i+1)  
            
            A=sorted(A)
            
        print(sum(cost))
