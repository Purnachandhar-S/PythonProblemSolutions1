import heapq
# normal way
array1 = [1,2,32,3,4,9]
# array = list(map(int,input().split()))
array1 = sorted(array1)
print(array1[-2])
print(array1)

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# Example usage
array1 = [3, 2, 1, 5, 6, 4]
sol = Solution()
result = sol.findKthLargest(array1, 2)
print(result)  # Output: 5


# …or create a new repository on the command line
# echo "# PythonProblemSolutions1" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Purnachandhar-S/PythonProblemSolutions1.git
# git push -u origin main


# …or push an existing repository from the command line
# git remote add origin https://github.com/Purnachandhar-S/PythonProblemSolutions1.git
# git branch -M main
# git push -u origin main
