class Solution:
    def longestPalindrome(self, s):
        res = ""

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

        for l in range(len(s)):
            tmp = helper(l, l)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(l, l+1)
            if len(tmp) > len(res):
                res = tmp

        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    
    # def longestPalindrome(self, s: str) -> str:

    #     res = ''
    #     for i, c in enumerate(s):
    #         l,r=i,i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r-l+1) > len(res):
    #                 res = s[l:r+1]
    #             l-=1
    #             r+=1
                
    #         l,r=i,i+1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r-l+1) > len(res):
    #                 res = s[l:r+1]
    #             l-=1
    #             r+=1

    #     return res 