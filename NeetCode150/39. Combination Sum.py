from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    stack = []
    ans = []

    def backtrack(total_sum=0, i=0):
        if total_sum > target:
            return
        elif total_sum == target:
            ans.append(list(stack))
        else:
            for j, candidate in enumerate(candidates[i:]):
                total_sum += candidate
                stack.append(candidate)
                backtrack(total_sum, j+i)
                stack.pop()
                total_sum -= candidate

    backtrack()
    print(ans)

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8

    combinationSum(candidates, target)