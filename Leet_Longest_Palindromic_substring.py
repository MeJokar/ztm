class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        s2 = list(s)
        s2.reverse()
        
        if len(s) ==1:
            return s
        elif len(s) == len(set(s)):
            return s[0]
        elif len(set(s)) == 1:
            return s
        equals = []
        index = 0
        for char1, char2 in zip(s1, s2):
            if char1 == char2: 
                equals.append(1)
            else:
                equals.append(0)
        l2 = [0]
        for i in range(1,len(equals)):
            if equals[i] != equals[i-1]:
                l2.append(i)
            elif equals[i] == equals[i-1] and i == (len(equals) -1): 
                l2[-1] = i
        max_length = 0 

        for i in range(1, len(l2)):
            if max_length < (l2[i] - l2[i-1]):
                tp = (l2[i] , l2[i-1])
                max_length = l2[i] - l2[i-1]
        print(tp, equals)
        return s[tp[1]: tp[0]]
    

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abb'))
