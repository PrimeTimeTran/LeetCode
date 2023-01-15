'''
Helper method moving i and j pointers thru text1 and text2 as needed.

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i, j, dic={}):
            if (i,j) in dic:
                return dic[(i,j)]
            elif i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                dic[(i,j)] = 1 + lcs(i+1,j+1)
            else:
                dic[(i,j)] = max(lcs(i+1,j), lcs(i,j+1))
            return dic[(i,j)]
        return lcs(0, 0)