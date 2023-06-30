class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            # print(stack, i)
            if stack:
                if stack[-1][1] > height:
                    while stack[-1][1] > height:
                        pos, past_height = stack.pop()
                        max_area = max(max_area, (i-pos)*past_height)
                        if not stack:
                            break
                    stack.append((pos, height))
                    continue
            stack.append((i, height))
        while stack:
            # print(stack)
            pos, height = stack.pop()
            max_area = max(max_area, ((i+1)-pos)*height)
            
            
        return max_area
