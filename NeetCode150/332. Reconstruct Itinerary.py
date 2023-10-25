from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj={}
        tickets.sort()
        for ticket in tickets:
            adj[ticket[0]]=deque()
            adj[ticket[1]]=deque()

        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        ans=[]
        def helper(node):
            while adj[node]:
                helper(adj[node].popleft())

            ans.append(node)
        helper("JFK")
        return reversed(ans)
