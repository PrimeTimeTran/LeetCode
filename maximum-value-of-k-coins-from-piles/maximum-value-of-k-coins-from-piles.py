class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @functools.lru_cache(None)
        def _search(rest_k: int, pile_pos: int) -> int:
            """Searches for best accumulated coin value starting from pile at position `pile_pos`.
            
            Args:
              - rest_k: The rest of coins we could pick.
              - pile_pos: The starting position of pile we are working on.
            """
            if rest_k == 0 or pile_pos == len(piles): return 0

            # Ignore the current pile and moving to next pile
            current_mv_found = _search(rest_k, pile_pos+1)

            # Start looking solution with current pile being involved
            current_pile = piles[pile_pos]
            accum_coin_value = 0
            for i in range(min(rest_k, len(current_pile))):
                # Accumulate the coins
                accum_coin_value += current_pile[i]

                # Moving to next pile with accumulated coin value in current pile
                current_mv_found = max(
                    current_mv_found, 
                    accum_coin_value + _search(rest_k-i-1, pile_pos+1))

            # Return the maximum accumulated coin value found from current pile.
            return current_mv_found

        # Start searching with initial `k` and first pile
        return _search(k, 0)