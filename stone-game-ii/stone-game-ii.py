class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) == 1:
            return piles[0]
        suffix_sum = self._suffix_sum(piles)

        dp = [[0] * (len(piles) + 1) for _ in range(len(piles) + 1)]

        for pile in reversed(range(len(piles))):
            for M in reversed(range(len(piles))):
                sum_next_player = suffix_sum[pile]

                for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                    sum_next_player = min(
                        sum_next_player, dp[next_pile][max(M, next_pile - pile)]
                    )

                sum_player = suffix_sum[pile] - sum_next_player

                dp[pile][M] = sum_player

        return dp[0][1]
    @staticmethod
    def _suffix_sum(piles: List[int]) -> List[int]:
        suffix_sum = [0]

        for pile in reversed(piles):
            suffix_sum.append(suffix_sum[-1] + pile)

        suffix_sum.reverse()

        return suffix_sum