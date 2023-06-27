def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    stack = []
    ans = [0] * len(temperatures)
    for i in range(len(temperatures)):
        # if not stack or temperatures[stack[-1]] > temperatures[i]:
        #     stack.append(i)
        # else:
        while(stack and temperatures[stack[-1]] < temperatures[i]):
            index = stack.pop()
            ans[index] = i-index
        stack.append(i)
    return ans

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    dailyTemperatures(temperatures)