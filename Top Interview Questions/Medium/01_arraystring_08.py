class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num):
            num_say = ""
            num = str(num)
            current = num[-1]
            current_count = 1
            for digit in num[::-1][1:]:
                print(digit)
                if digit == current:
                    current_count += 1
                else:
                    num_say = str(current_count) + current + num_say
                    current = digit
                    current_count = 1
            

            return int(str(current_count) + current + num_say)

        result = 1
        for i in range(2, n+1):
            result = say(result)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))