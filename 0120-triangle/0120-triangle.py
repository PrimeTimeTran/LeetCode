class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        distance = triangle[0]*height
        for h in range(1,height):
            for i in range(h,-1,-1):
                choose_path = min(distance[max(i-1,0):min(i+1,h)])
                distance[i] = triangle[h][i] + choose_path
        return min(distance)