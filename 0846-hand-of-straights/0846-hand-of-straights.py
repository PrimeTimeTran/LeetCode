'''
This is a greedy algorithm that always forms sequences starting from the smallest available card, which is a forced and safe choice.
Each copy of the smallest card starts a straight, so I must consume the same number of copies from every consecutive value to complete those straights.
'''
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0: return False
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        for k in sorted_keys:
            for i in range(1, groupSize):
                if count[k] > 0:
                    if count[k] > count[k+i]:
                        return False
                    count[k+i] -= count[k]
        return True