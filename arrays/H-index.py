class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        arr = [0]*(n + 1)
        for citation in citations:
            i = min(citation,n)
            arr[i] += 1
        count = 0
        for i in range(n,-1,-1):
            count += arr[i]
            if i <= count: return i
