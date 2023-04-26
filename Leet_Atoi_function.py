class Solution(object):
    # def myAtoi(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     signs = ['-', '+']
    #     digits = '0123456789'
    #     cap_min = -2**32
    #     cap_max =  2**32


    #     if len(s) == 0:
    #         return 0
    #     elif len(s) == 1 and s in digits:
    #         return int(s)
    #     elif len(s) == 1 and s not in digits:
    #         return 0
    #     ints = []
    #     sign = None
    #     break_condition = False 
    #     for char in s:
    #         if char in signs: 
    #             sign = str(char)
    #         elif char in digits: 
    #             ints.append(char)
    #             break_condition = True
    #         if char not in digits and break_condition:
    #             break
    #     if not ints:
    #         return None
    #     elif sign == '+' or sign == None:
    #         return min (int(''.join(ints)), max_cap)
    #     elif sign == '-':
    #         return max(-1*int(''.join(ints)) , min_cap)
    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = len(str)
        while pos < ls and str[pos] == ' ':
            pos += 1
        if pos < ls and str[pos] == '-':
            sign = -1
            pos += 1
        elif pos < ls and str[pos] == '+':
            pos += 1
        print(pos)
        while pos < ls and ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
            num = ord(str[pos]) - ord('0')
            if result > max_int / 10 or ( result == max_int / 10 and num >= 8):
                if sign == -1:
                    return min_int
                return max_int
            result = result * 10 + num
            pos += 1

        return sign * result
    
    def myAtoi(self, s):
        #https://leetcode.com/discuss/83626/line-python-solution-eafp-instead-lbyl-easier-logic-beats-24%25
        try:
            s = s.lstrip() + '$' # remove leading spaces and append an end mark
            for i, ch in enumerate(s):
                if not (ch in '+-' or '0' <= ch <= '9'):
                    print(ch)
                    result = int(s[:i])
                    return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
        except:
            return 0


S =Solution()

print(S.myAtoi("words and 987"))
print(max(-10, -2))