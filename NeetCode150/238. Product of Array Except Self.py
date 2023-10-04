class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        len_num = len(nums)
        for i in range(len_num):
            prefix.append(prefix[i]*nums[i])
            postfix.insert(0, postfix[-(i+1)]*nums[-(i+1)])
        product_except_self = []
        for i in range(len_num):
            product_except_self.append(prefix[i] * postfix[i+1])
        return [prefix[i] * postfix[i+1] for i in range(len_num)]
