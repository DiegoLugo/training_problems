#1791. Find Center of Star Graph
#https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges: list[list[int]]):
        edge1, edge2 = edges[0], edges[1]
        
        return edge1[0] if edge1[0] in edge2 else edge1[1] 


if __name__ == '__main__':
    print(Solution().findCenter([[1,2],[2,3],[4,2]]))