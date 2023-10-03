class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = num_dict.get(nums[i], []) + [i]
        
        for i in range(len(nums)):
            proxy_target = target - nums[i]
            if proxy_target in num_dict:
                if proxy_target == nums[i]:
                    if len(num_dict[proxy_target]) == 1:
                        continue
                    else:
                        return i, num_dict[proxy_target][1]
                else:
                    return i, num_dict[proxy_target][0]
                
        
