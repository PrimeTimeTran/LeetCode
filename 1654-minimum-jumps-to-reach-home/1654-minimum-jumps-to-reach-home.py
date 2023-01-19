class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        boundary = x + a + b + max(forbidden)
        f = set(forbidden)
        q = deque([(0, False)])  # position, last-backward
        level = 0
        seen = set([(0, False)])
        while q:
          n = len(q)
          for _ in range(n):
            cur, back = q.popleft()
            if cur == x: 
              return level
            next_pos = cur + a
            # important to check the "next_pos < boundary", otherwise TLE
            if next_pos not in f and next_pos < boundary and (next_pos, False) not in seen:
              q.append((next_pos, False))
              seen.add((next_pos, False))
            
            next_pos = cur - b
            if next_pos >= 0 and not back and next_pos not in f and (next_pos, True) not in seen:
              q.append((next_pos, True))
              seen.add((next_pos, True))
          
          level += 1
        
        return -1