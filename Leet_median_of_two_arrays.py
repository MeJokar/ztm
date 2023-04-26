class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def med(l1):
            if len(l1) % 2 == 0:
                return (l1[len(l1)//2-1]+l1[len(l1)//2])/2
            else:
                return l1[len(l1)//2]

        if len(nums1) == 0 and len(num2) == 0:
            return None
        elif len(nums1) == 0:
            return med(nums2)
        elif len(nums2) == 0:
            return med(nums1)
        else: 
            nums3 = nums1 + nums2
            nums3.sort()
            print(nums3)
            return med(nums3)
        
if __name__ == "__main__":
    l1 = [1,2]
    l2 = [3,4]
    S = Solution()
    print(S.findMedianSortedArrays(l1,l2))
    ss = list('abc')
    print('#'.join(f'{ss}'))

    s1 = list('abca')
    s2 = list('abca')
    s2.reverse()
    # print(s1, s2, s1 == 'a')
    for i in range(1,1):
        print(i)
