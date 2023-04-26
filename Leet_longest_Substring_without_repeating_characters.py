class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        max_length = 0
        start = 0
        # temp_length = 0
        # for char in s: 
        #     if char_dict.get(char) == None:
        #         char_dict[char] = 1
        #         temp_length +=1
        #         max_length = max(temp_length, max_length)
        #     elif char_dict.get(char) != None:
        #         del char_dict
        #         char_dict = {}
        #         max_length = max(temp_length, max_length)
        #         temp_length = 0
        for index, char in enumerate(s): 
            print(char, f'start = {start}, index = {index}, max_len = {max_length}')
            if char in char_dict and char_dict.get(char, -1) >= start:
                start = char_dict[char] + 1
            print(char, f'start = {start}, index = {index}, max_len = {max_length}', '\n')
            char_dict[char] = index
            max_length = max(max_length, index - start + 1)
            # print(start, index, max_length,  index - start + 1, 'here')

        return max_length
   
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abbcabcb'))
    # print(s.lengthOfLongestSubstring('abbbabb'))
