from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        reference_set = set(nums1)
        
        count_dict = {}

        for item in nums1:
            count_dict[item] = count_dict.get(item, 0) + 1
        
        result_list = []

        for item in nums2:
            item_count = count_dict.get(item, 0)
            
            if item_count:
                result_list.append(item)
                count_dict[item] = item_count-1

        return result_list



if __name__ == '__main__':
    params = ([1,2,2,1], [2,2])
    s = Solution()
    print(s.intersect(*params))