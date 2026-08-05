from collections import defaultdict
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        print(graph)
        for u,v in invocations:
            graph[u].append(v)
        suspicious = set()

        def dfs(node):
            suspicious.add(node)
            for i in graph[node]:
                if i not in suspicious:
                    dfs(i)

        dfs(k)
        for u,v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        ans  = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans